"""
Module for migrants (immigrants and refugees)
"""
from matching.user import User
from matching.mentor import Mentor

class Migrant(User):
	"""
	Class for a migrant that can be used for the matching system.
	"""

	def __init__(self):
		super(Migrant, self).__init__()
		self.__status = ""
		self.match: Mentor = None
		
	def set_status(self, status):
		self.__status = status
	
	def get_status(self):
		return self.__status
	
