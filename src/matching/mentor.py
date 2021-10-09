"""
Module for mentors with certain parameters to find
their ideal mentees as they come into the country
"""

from typing import List, Tuple, Dict

class Mentor(object):
	"""
	Class for a mentor instantiated when data is processed from a user.
	"""

	def __init__(self):
		"""
		Inititiation for the mentor class.
		"""
		self.country: str = ""
		self.name: str = ""
		self.description:  str = ""
		self.languages : List[str]  = []
		self.location: Tuple[float] = ()
		self.demographics: Dict[str : str] = {}
		self.interests_keys: List[str] = []

		
