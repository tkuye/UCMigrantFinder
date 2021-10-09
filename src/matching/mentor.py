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
		self.__matches: List[Migrant] = []
		self.match: Migrant = None

	def add_matches(self, migrants: List[Migrant]):
		"""
		Adds matches to a following mentor
		Args:
			migrants (List[Migrant]): The list of migrants to add
		"""
		i = 0 
		while len(self.__matches) <= self.max_matches:
			self.__matches.append(migrants[i])
			i += 1
