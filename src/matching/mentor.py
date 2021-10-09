"""
Module for mentors with certain parameters to find
their ideal mentees as they come into the country
"""

from typing import List
from matching.user import User
from matching.migrant import Migrant

class Mentor(User):
	"""
	Class for a mentor object.
	"""

	def __init__(self):
		"""
		Initiates the class for a Mentors
		"""
		super(Mentor, self).__init__()

		self.max_matches = 10
		self.matches: List[Migrant] = []

	
