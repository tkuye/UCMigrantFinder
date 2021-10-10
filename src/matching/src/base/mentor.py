"""
Module for mentors with certain parameters to find
their ideal mentees as they come into the country
"""

from typing import List
from .user import User
from .migrant import Migrant

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


	def add_matches(self, migrants: List[Migrant]):
		"""
		Adds matches to a following mentor
		Args:
			migrants (List[Migrant]): The list of migrants to add
		"""
		i = 0 
		while len(self.__matches) <= self.max_matches and i < len(migrants):
			self.__matches.append(migrants[i])
			i += 1

	def get_matches(self):
		"""Gets all matches for a mentor
		"""
		return self.__matches

	def to_dict(self):
		"""
		Converts a mentor into a dictionary
		"""
		mentor = {
			"country": self.get_country(),
			"name": self.get_name(),
			"description": self.get_description(),
			"languages": self.get_languages(),
			"location": self.get_location(),
			"demographics": self.get_demographics(),
			"interests": self.get_interests(),
			"match": self.get_match(),
			"room": self.get_room(),
			"id":self.id,
		}
		return mentor

	@staticmethod
	def dict_to_mentor(mentor_dict: dict):
		"""Converts a dictionary into mentor class object
		Args:
			mentor_dict (dict): The dictionary to convert
		"""

		mentor = Mentor()
		mentor.set_country(mentor_dict.get("country"))
		mentor.set_name(mentor_dict.get("name"))
		mentor.set_demographics(mentor_dict.get("demographics"))
		mentor.set_languages(mentor_dict.get("languages"))
		mentor.set_location(mentor_dict.get("location"))
		mentor.set_interests(mentor_dict.get("interests"))
		mentor.set_match(mentor_dict.get("match"))
		mentor.set_room(mentor_dict.get("room"))
		mentor.id = str(mentor_dict.get("_id"))
	
		return mentor