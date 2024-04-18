import numpy as np
import miro2 as miro
from . import action_types

class ActionFace(action_types.ActionTemplate):
    def finalize(self):
		
		# parameters
		self.name = "face"
		self.retreatable = True
                
    def compute_priority(self):

		priority = 1
		
		# ok
		return priority
	
    def service(self):
		# -----