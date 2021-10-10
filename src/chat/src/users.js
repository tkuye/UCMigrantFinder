const {MongoClient} = require('mongodb');

const url = "mongodb://localhost:27017"
const client = new MongoClient(url);

module.exports = {
	users = new Map(),
	
	getRoom  = async (user_id, callback) => {
		await client.connect();
		let db = await client.db("ucmfinder");
		let migrants = db.collection("migrants");
		let mentors = db.collection("mentors");

		mentors.findOne({_id: user_id}, function (err, result) {
			if (err) throw err;
			return callback(result.room);
		})
		migrants.findOne({_id: user_id}, function (err, result) {
			if (err) throw err;
			return callback(result.room);
		})
		
		client.close()
	},


	addPayload = async (payload) => {
		await client.connect();
		let db = await client.db("ucmfinder");
		let chats = db.collection("chats");
		chats.insertOne(payload).catch(err => {
			console.error(err);
		})
		client.close();
	},

	getChatData = async (room_id, callback) => {
		await client.connect();
		let db = await client.db("ucmfinder");
		let chats = db.collection("chats");
		chats.find({room_id: room_id}, function (err, result) {
			if (err) throw err
			return callback(result)
		})
	},

	addUser = (socket_id, room) => {
		users[socket_id] = room;
	},

	getUser = (socket_id) => {
		return users[socket_id];
	},

	removeUser = (socket_id) => {
		users.delete(socket_id);
	}

}




