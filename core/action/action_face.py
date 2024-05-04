import numpy as np
import miro2 as miro
from . import action_types
import random
from subscriber_cam import CamSubscriber 
class ActionFace(action_types.ActionTemplate):


    def finalize(self):

        # parameters
        self.name = "face"
        self.retreatable = True

    def compute_priority(self):
        
        # valence = self.input.emotion.valence
        # arousal = self.input.emotion.arousal

        priority = 1

        return priority
        # return self.move_softsat(self.input.priority_peak.height)

    def start(self):

        face = CamSubscriber()

        
        print(CamSubscriber.callback_cam)

        
        # default
        steps = 200

        # +ve valence boost
        self.system_state.action_target_valence = 0.2
        
        # start action clock
        self.clock.start(steps)


    def service(self):

        
        # # get constants
        # c = miro.constants

        # # read clock
        # x = self.clock.cosine_circle_profile()
        # y = self.clock.sine_profile()
        # z = self.clock.cosine_profile()
        # self.clock.advance(True)

        # # circle
        # config = self.kc.getConfig()
        # config[1] = c.LIFT_RAD_MIN + x * (c.LIFT_RAD_MAX - c.LIFT_RAD_MIN)
        # config[2] = c.YAW_RAD_MAX * y
        # config[3] = c.PITCH_RAD_MAX + x * (c.PITCH_RAD_MIN - c.PITCH_RAD_MAX)
        # #print (config)
        # self.kc.setConfig(config)

        # # open eyes
        # self.system_output.cosmetic_joints[2] = 0.0
        # self.system_output.cosmetic_joints[3] = 0.0
        pass
    def stop(self):
        pass

    def ascending(self):

        # default ascending() behaviour is to compute action priority

        # if selected
        if self.interface.inhibition == 0:

            # raise priority if motor pattern is ongoing
            if self.clock.isActive():

                # ongoing priority must initially be at least the same priority
                # to avoid rapid behavioural switching between two actions
                # that both have high priorities given the current stimulus;
                # over time it can decay, allowing an interrupt to occur in
                # principle, though it rarely would in practice since the
                # ongoing_priority is usually still rather high.
                self.interface.priority = max(self.interface.priority * 0.99, self.ongoing_priority)

            # if not, no longer want the plant
            else:

                # zero priority
                self.interface.priority = 0.0

        else:

            # compute priority from inputs
            self.interface.priority = self.compute_priority()
# set the priority here
    def descending(self):

        # default descending() behaviour is to start/stop as required
        # and service an ongoing motor pattern if there is one

        # if motor plan is active
        if self.clock.isActive():

            # if inhibited
            if self.interface.inhibition > 0:

                # stop motor plan
                self.stop()

            # otherwise
            else:

                # service motor plan
                self.service()

        # if motor plan is not active
        else:

            # if disinhibited
            if self.interface.inhibition == 0:

                # debug
                if self.debug:
                    self.input.dump()

                # start motor plan
                self.start()