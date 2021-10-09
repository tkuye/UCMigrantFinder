"""
Base module for all users
"""

from typing import List, Tuple, Dict

class User(object):
	"""
	Class for a mentor instantiated when data is processed from a user.
	"""

	def __init__(self):
		"""
		Inititiation for the mentor class.
		"""
		self.__country: str = ""
		self.__name: str = ""
		self.__description:  str = ""
		self.__languages : List[str]  = []
		self.__location: Tuple[float] = ()
		self.__demographics: Dict[str: str] = {}
		self.__interests_keys: List[str] = []
		self.__photo_url: str = ""


	def get_country(self) -> str:
		"""Gets the country of the user

		Returns:
			str: country
		"""
		return self.__country

	
	def set_country(self, country):
		"""Sets the country of the user"""

		self.__country = country

	def get_name(self) -> str:
		"""Gets the user's name

		Returns:
			str: name
		"""
		return self.__name

	def set_name(self, name) -> None:
		"""Sets the name of the user

		Args:
			name: The name of a user
		"""
		self.__name = name

	def get_description(self) -> str:
		"""
		Gets a user's description
		Returns:
			str
		"""
		return self.__description
	
	def get_language(self, language: str) -> bool:
		"""Checks if a user speaks a certain language

		Args:
			language (str): The language spoken

		Returns:
			bool: True or false if the language is spoken 
		"""
		return language in self.__languages


	def set_language(self, language:str) -> None:
		"""
		Sets a language for the user

		Args:
			language (str): The language for the user
		"""
		if language not in self.__languages:
			self.__languages.append(language)

	def get_languages(self) -> List[str]:
		"""Gets a list of languages for the user

		Returns:
			List[str]: language
		"""
		return self.__languages

	def get_location(self) -> Tuple:
		"""Gets our location for our user (lat, long)

		Returns:
			Tuple: The latitude and longitude of a user
		"""
		return self.__location

	def get_lat(self) -> float:
		"""Gets a user's latitude

		Returns:
			float: Latitude of the user
		"""
		return self.__location[0]

	def get_long(self) -> float:
		"""
		Gets a longitude for a user

		Returns:
			float: longitude of a user
		"""
		return self.__location[1]

	def set_demographic(self, name:str, description:str) -> None:
		"""
			Sets a demographic for a target user
		Args:
			name (str): the name of the demographic
			description (str): the description of a demographic
		"""
		self.__demographics[name] = description
	

	def get_interest(self, interest) -> bool:
		"""
		Checks a user for a certain interest

		Args:
			interest (string): The description of the user interest

		Returns:
			bool: Returns true if the user has a same interest.
		"""
		return interest in self.__interests_keys

	def get_interests(self) -> List[str]:
		"""
		Gets all user interests

		Returns:
			List[str]: a list of a users interests. 
		"""
		return self.__interests_keys

	def set_interest(self, interest) -> None:
		"""Sets a user interest for a certain interest

		Args:
			interests ([type]): [description]
		"""

		if interest not in self.__interests_keys:
			self.__interests_keys.append(interest)


	def get_demographic(self, demographic) -> str:
		"""
			Gets a user demographic.
		
		Args:
			demographic: a certain demographic name

		Returns:
			str: The data associated with a demographic
		"""
		demo = self.__demographics.get(demographic)

		if demo is not None:
			return demo
		else:
			return ""

	def get_demographics(self):
		"""
		Gets all of a user's demographics
		"""

		return self.__demographics


	def set_photo_url(self, url) -> None:
		"""
		Sets the url of a photo

		Args:
			url (str): The url of a photo
		"""
		self.__photo_url = url


	def get_photo_url(self):
		"""Returns a photo url for a user

		Returns:
			[type]: [description]
		"""
		return self.__photo_url

