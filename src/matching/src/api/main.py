"""
The main api module point
"""

from flask import Flask, request, jsonify, session, abort
from flask_cors import CORS
from src.models.main import Database

db = Database("mongodb://localhost:27017", "ucmfinder")

app = Flask(__name__)
cors = CORS(app)
app.secret_key = "UCHACKATHON"

@app.route("/create-user", methods=["POST"])
def create_user():
	"""
	Creates a new user.
	"""
	data = request.json
	username = db.create_user(data.get("username"), data.get("password"))
	session["username"] = username
	return username, 200

@app.route("/check-user", methods=["POST"])
def check_user():
	"""
	Checks a user and password
	"""
	data = request.json
	if not db.get_user(data.get("username"), data.get("password")):
		abort(401)
	return "", 201

@app.route("/new-migrant", methods=['POST'])
def new_migrant():
	"""
	Adds new migrant to the database.
	"""
	
	_id = db.add_new_migrant(request.json)
	session["id"] = _id
	return jsonify({"id":_id, "status":"migrant"}), 201

@app.route("/new-mentor", methods=['POST'])
def new_mentor():
	"""
	Adds new mentor to the database.
	"""
	_id = db.add_new_mentor(request.json)
	session["id"] = _id
	return jsonify({"id":_id, "status":"mentor"}), 201

@app.route("/get-migrants/<mentor_id>", methods=['GET'])
def get_migrants(mentor_id):
	"""
	Gets all the migrants for a mentor
	"""

	return jsonify(db.find_migrants(mentor_id))

@app.route("/select-migrant/<migrant_id>/<mentor_id>", methods=['POST'])
def select_migrant(migrant_id, mentor_id):
	"""
	Selects a migrant for a given mentor
	"""
	room = db.select_migrant(mentor_id, migrant_id)
	return jsonify({"room": room}), 201

@app.route("/select-mentor/<mentor_id>/migrant_id", methods=['POST'])
def select_mentor(mentor_id, migrant_id):
	"""
	Selects a mentor for a given migrant
	"""
	db.select_mentor(mentor_id, migrant_id)
	return "", 201

@app.route("/get-migrant/<migrant_id>", methods=['GET'])
def get_migrant(migrant_id):
	"""
		Gets a migrant for a given id
	"""
	return jsonify(db.get_mentor(migrant_id))

@app.route("/get-matched-mentors/migrant_id", methods=['GET'])
def get_matched_mentors(migrant_id):
	"""
	Gets a migrant mentors.
	"""
	return jsonify(db.get_matched_mentors(migrant_id))

@app.route("/get-mentor/<mentor_id>", methods=['GET'])
def get_mentor(mentor_id):
	"""
	Gets a mentor for a given id
	"""
	return jsonify(db.get_mentor(mentor_id))



def main():
	"""
	Main function of flask app.
	"""
	app.run(debug=True)

if __name__ == "__main__":
	main()