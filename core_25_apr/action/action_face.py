import numpy as np
import miro2 as miro
from . import action_types

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

	def start(self):

		

    def service(self):
		# -----