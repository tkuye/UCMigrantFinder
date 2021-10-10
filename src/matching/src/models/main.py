import pymongo 
from src.base.matcher import Matcher
import random
import string

class Database(object):
	"""
	Class for the database.
	"""

	def __init__(self, db_url: str, db_name:str):
		self.__db_url = db_url
		self._db = self.__init_db(db_name)
		self.migrants = self._db["migrants"]
		self.mentors = self._db["mentors"]
		self.matcher = self.__init_matcher()
		
	def __init_matcher(self):
		"""
		Initiates the matcher class

		Returns:
			[type]: [description]
		"""
		matcher = Matcher()
		matcher.set_mentors(self.mentors.find())
		matcher.set_migrants(self.migrants.find())
		return matcher

	def __init_db(self, db_name):
		"""Initiates a new database connection
		Args:
			db_name ([type]): name of the database you want to connect or create
		"""
		client = pymongo.MongoClient(self.__db_url)
		return client[db_name]

	def get_migrant(self, migrant_id:str):
		"""
			Gets the migrant with a specified id
		Args:
			migrant_id (str): the migrant id
		"""
		migrant = self.matcher.get_mentor(migrant_id)
		if migrant is not None:
			return migrant.to_dict()
		
	def get_mentor(self, mentor_id):
		"""
			Gets the mentor with a specified id
		Args:
			mentor_id (str): the mentor id
		"""
		
		
		mentor = self.matcher.get_mentor(mentor_id)
		if mentor is not None:
			return mentor.to_dict()


	def find_migrants(self, mentor_id:str):
		"""
		Finds the given migrants for a specified mentor
		Args:
			mentor_id (str): The mentor id
		"""
		mentor = self.matcher.get_mentor(mentor_id)
		if mentor is None:
			return []
		self.matcher.find_matches(mentor)
		
		migrants = []
		for migrant in mentor.get_matches():
			migrants.append(migrant.to_dict())
		
		return migrants

	def add_new_migrant(self, migrant_dict:dict):
		"""
			Adds a migrant to mongo db and matcher system
		Args:
			migrant_dict (dict): the migrant
		"""
		self.migrants.insert_one(migrant_dict)
		self.matcher.add_migrant(migrant_dict)

	def add_new_mentor(self, mentor_dict:dict):
		"""
		Adds a new mentor to the mongo db and matcher system.
		"""
		self.mentors.insert_one(mentor_dict)

		self.matcher.add_mentor(mentor_dict)

	def select_mentor(self, mentor_id:str, migrant_id: str):
		"""
		Select a mentor for a specified user

		Args:
			mentor_id (str)
			migrant_id (str)
		"""
		mentor = self.matcher.get_mentor(mentor_id)
		mentor.set_match(migrant_id)

		self.mentors.update_one(Database.id_query(mentor_id), {"match": migrant_id})

	def select_migrant(self, mentor_id, migrant_id):
		"""
		Select a migrant for a specified user
		Args:
			mentor_id (str)
			migrant_id (str)
		"""
	
		migrant = self.matcher.get_migrant(migrant_id)
		mentor = self.matcher.get_mentor(mentor_id)
		migrant.set_match(mentor_id)
		room = Database.random_char(10)
		migrant.set_room(room)
		mentor.set_room(room)
		
		self.migrants.update_one(Database.id_query(migrant_id), {"match": mentor_id})
		self.mentors.update_one(Database.id_query(mentor_id), {"room": room})
		self.migrants.update_one(Database.id_query(migrant_id), {"room": room})

	@staticmethod
	def id_query(id:str):
		return {"_id": id}
	

	@staticmethod
	def random_char(y):
		return ''.join(random.choice(string.ascii_letters) for x in range(y))