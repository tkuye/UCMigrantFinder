"""
The matching system itself
"""
from typing import Dict, List, Tuple
from matching.mentor import Mentor
from matching.migrant import Migrant

class Matcher(object):
	"""
	Class for a matcher system
	"""

	def __init__(self):
		"""
		Initial class constructor for the matcher class
		"""
		self.mentors: Dict[str, Mentor] = {}
		self.migrants: List[Migrant] = []

	def find_matches(self, mentor: Mentor) -> List[Migrant]:
		"""
		Finds matches based on certain criteria for a given Mentor
		Args:
			Mentor ([type]): [description]
		"""
		usable_migrants = self.__find_matches_on_country(mentor.get_country())

		existing = dict()
		migrants = list()
		# If this number is less than the max available then we must return
		if len(usable_migrants) < mentor.max_matches:
			return usable_migrants
		
		# The names correspond to the weights of each group of migrants
		m0 = self.__find_matches_on_location(mentor.get_location(), usable_migrants)
		m1 = self.__find_matches_on_language(mentor.get_language(), usable_migrants)
		m2 = self.__find_matches_on_interest(mentor.get_interests(), usable_migrants)
		m3 = self.__find_matches_on_demographic(mentor.get_demographics(), usable_migrants)
		
		self.__add_migrants(m0, migrants, existing)
		self.__add_migrants(m1, migrants, existing)
		self.__add_migrants(m2, migrants, existing)
		self.__add_migrants(m3, migrants, existing)


		return migrants
	
	def __add_migrants(self, migrants: List[Migrant], total_migrants:List[Migrant], existing: dict):
		
		for item in migrants:
			if item in existing:
				ItemNumber = existing[item]
			else:
				migrants.append(item)
				existing[item] = ItemNumber = len(migrants) - 1

			
	def __find_matches_on_interest(self, interests: List[str], possible_migrants: List[Migrant]) -> List[Migrant]:
		"""Private function for finding migrants based on similar interests
		Args:
			interests (List[str]): list of interests
			possible_migrants (List[Migrant]): possible migrants based on a country

		Returns:
			List[Migrant]: List of migrants
		"""
		findable_migrants = set()
		for interest in interests:
			for migrant in possible_migrants:
				if migrant.get_interest(interest):
					findable_migrants.add(migrant)
		return list(findable_migrants)

	def __find_matches_on_country(self, country: str) -> List[Migrant]:
		"""Private function for finding migrants for based on a given country

		Args:
			country (str): the country of the mentor

		Returns:
			List[Migrant]: The list of countries found
		"""
		findable_migrants = []

		for migrant in self.migrants:
			if migrant.get_country() == country:
				findable_migrants.append(migrant)
		
		return findable_migrants

	def __find_matches_on_demographic(self, demographic: Dict[str, str], possible_migrants: List[Migrant]) -> List[Migrant]:
		findable_migrants = set()
		
		for key in demographic.keys():
			for migrant in possible_migrants:
				if migrant.get_demographic(key):
					findable_migrants.add(migrant)


		return list(findable_migrants)
	
	def __find_matches_on_language(self, languages: List[str], possible_migrants: List[Migrant]) -> List[Migrant]: 
		"""Private function for finding migrants based on a given language

		Args:
			language (str): the language spoken
			possible_migrants (List[Migrant]): [description]

		Returns:
			List[Migrant]: [description]
		"""
		findable_migrants = set()

		for migrant in possible_migrants:
			for language in languages:
				if migrant.get_language() == language:
					findable_migrants.add(migrant)

		return list(findable_migrants)



	def __find_matches_on_location(self, location: Tuple[float], possible_migrants:List[Migrant], distance: float = 1):
		"""Private function for finding migrants within a given location
		Defaulted to one latitudinal point
		Args:
			location (Tuple[float]): Latitude and longitude of the mentor
			possible_migrants (List[Migrant]): list of possible_migrants
			distance (float, optional): [description]. Defaults to 1.
		"""
	
		findable_migrants = []
		for migrant in possible_migrants:
			if migrant.get_lat() -location[0] < distance and migrant.get_long() - location[1] < distance:
				findable_migrants.append(migrant)

		return findable_migrants

	
