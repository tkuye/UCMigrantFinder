"""
Module for migrants (immigrants and refugees)
"""

from .user import User

class Migrant(User):
	"""
	Class for a migrant that can be used for the matching system.
	"""

	def __init__(self):
		super(Migrant, self).__init__()
		self.__status = ""
		self.match: str = ""
		self.__countries = []
	

	def set_countries(self, countries):
		"""
		Setter for our countries
		"""
		self.__countries = countries.copy()
	
	def get_countries(self):
		"""
		Gets our countries as a list
		"""
		return self.__countries
	def set_status(self, status:str):
		"""
		Sets the status for a migrant as refugee or immigrant
		Args:
			status (str): refugee or immigrant
		"""
		self.__status = status

	def get_status(self):
		"""
		Gets the status for a given migrant
		Returns:
			str: The migrant status
		"""
		return self.__status


	def to_dict(self):
		"""Converts migrant into a dictionary
		"""
		migrant = {
			"countries": self.get_countries(),
			"name": self.get_name(),
			"description": self.get_description(),
			"languages": self.get_languages(),
			"location": self.get_location(),
			"demographics": self.get_demographics(),
			"interests": self.get_interests(),
			"status": self.get_status(),
			"match": self.get_match(),
			"room": self.get_room(),
		}

		return migrant


	@staticmethod
	def dict_to_migrant(migrant_dict: dict):
		"""
		Converts a dictionary into a Migrant object

		Args:
			migrant_dict (dict): the dictionary to convert
		"""
		migrant = Migrant()
		migrant.set_countries(migrant_dict.get("countries"))
		migrant.set_name(migrant_dict.get("name"))
		migrant.set_demographics(migrant_dict.get("demographics"))
		migrant.set_languages(migrant_dict.get("languages"))
		migrant.set_location(migrant_dict.get("location"))
		migrant.set_interests(migrant_dict.get("interests"))
		migrant.set_match(migrant_dict.get("match"))
		migrant.set_room(migrant_dict.get("room"))
