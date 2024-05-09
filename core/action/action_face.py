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

		steps = 250

		self.test = CamSubscriber()

		# compute start point for fovea in WORLD
		self.fovea_i_WORLD = self.kc.changeFrameAbs(miro.constants.LINK_HEAD, miro.constants.LINK_WORLD, self.fovea_HEAD)

		# compute end point for fovea in WORLD
		fovea_f_WORLD = self.kc.changeFrameAbs(
				miro.constants.LINK_HEAD,
				miro.constants.LINK_WORLD,
				miro.lib.kc_interf.kc_viewline_to_position(
					self.input.priority_peak.azim,
					self.input.priority_peak.elev,
					self.input.priority_peak.range
					)
				)

		# limit end point to be reachable
		fovea_f_WORLD[2] = np.clip(fovea_f_WORLD[2],
							self.pars.geom.reachable_z_min,
							self.pars.geom.reachable_z_max
							)

		# compute total movement fovea will make in world
		self.dfovea_WORLD = fovea_f_WORLD - self.fovea_i_WORLD

		# compute pattern time
		total_dist = np.linalg.norm(self.dfovea_WORLD)
		secs_ideal = total_dist * self.pars.action.approach_speed_spm
		steps_ideal = int(secs_ideal * self.pars.timing.tick_hz)
		steps_constrained = np.clip(steps_ideal,
					self.pars.action.approach_min_steps,
					self.pars.action.approach_max_steps
					)

		# start pattern
		self.clock.start(steps_constrained)

		# debug
		if self.debug:
			print ("fovea_i_WORLD", self.fovea_i_WORLD)
			print ("fovea_f_WORLD", fovea_f_WORLD)
			print ("pattern time", total_dist, secs_ideal, steps_ideal, steps_constrained)

		
		# CamSubscriber()
		

		# emotion = face.emotion_prediction   
		# print("asdasdadasd")

		# print(emotion)
		
		# default


		
		# start action clock
		self.clock.start(steps)


	def service(self):

		emotion = self.test.emotion_prediction

		c = miro.constants
		# read clock
		x = self.clock.cosine_circle_profile()
		y = self.clock.sine_profile()
		z = self.clock.cosine_profile()
		self.clock.advance(True)

		if emotion == "happy":
			x = self.clock.cosine_profile()

			# compute an interim target along a straight trajectory
			fovea_x_WORLD = x * self.dfovea_WORLD + self.fovea_i_WORLD

			# transform interim target into HEAD for actioning
			fovea_x_HEAD = self.kc.changeFrameAbs(miro.constants.LINK_WORLD, miro.constants.LINK_HEAD, fovea_x_WORLD)

			# apply push
			self.apply_push_fovea(fovea_x_HEAD - self.fovea_HEAD)
			print(emotion)
			# print(self.system_state.action_target_valence)   # print the valence score
		elif emotion == "neutral":
			print(emotion)
			# self.clock.advance(True)
		elif emotion == "angry":
			# read clock
			x = self.clock.cosine_profile()
			# self.clock.advance(True)

			# compute an interim target along a straight trajectory
			fovea_x_WORLD = x * self.dfovea_WORLD + self.fovea_i_WORLD

			# transform interim target into HEAD for actioning
			fovea_x_HEAD = self.kc.changeFrameAbs(miro.constants.LINK_WORLD, miro.constants.LINK_HEAD, fovea_x_WORLD)

			# apply push
			self.apply_push_fovea(fovea_x_HEAD - self.fovea_HEAD)
			print (emotion)
		elif emotion == "sad":
			# +ve valence boost
			self.system_state.action_target_valence = 0.2

			# circle
			config = self.kc.getConfig()
			config[1] = c.LIFT_RAD_MIN + x * (c.LIFT_RAD_MAX - c.LIFT_RAD_MIN)
			config[2] = c.YAW_RAD_MAX * y
			config[3] = c.PITCH_RAD_MAX + x * (c.PITCH_RAD_MIN - c.PITCH_RAD_MAX)
			#print (config)
			self.kc.setConfig(config)

			# open eyes
			self.system_output.cosmetic_joints[2] = 0.0
			self.system_output.cosmetic_joints[3] = 0.0
			print(emotion)
		elif emotion == "surprise":
			# quadrant time
			t = self.clock.t_norm * 4.0
			q = int(t)
			t -= q

			# profiles
			x = 0.5 - 0.5 * np.cos(t * np.pi)

			# do quadrant
			config = self.kc.getConfig()
			if q == 0:
				config[1] = c.LIFT_RAD_MIN + x * (c.LIFT_RAD_MAX - c.LIFT_RAD_MIN)
				config[2] = 0.0
				config[3] = c.PITCH_RAD_MIN + x * (c.PITCH_RAD_MAX - c.PITCH_RAD_MIN)
			if q == 1:
				config[2] = c.YAW_RAD_MAX * x * 1
			if q == 2:
				config[1] = c.LIFT_RAD_MIN + (1.0 - x) * (c.LIFT_RAD_MAX - c.LIFT_RAD_MIN)
				config[3] = c.PITCH_RAD_MIN + (1.0 - x) * (c.PITCH_RAD_MAX - c.PITCH_RAD_MIN)
			if q == 3:
				config[2] = c.YAW_RAD_MAX * (1.0 - x) * 1
			self.kc.setConfig(config)

			# close eyes
			self.system_output.cosmetic_joints[2] = 1.0
			self.system_output.cosmetic_joints[3] = 1.0
			print(emotion)
		elif emotion == "fear":
			print(emotion)
		elif emotion == "digust":
			print(emotion)
		else:
			
			print(emotion)
		   


		
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