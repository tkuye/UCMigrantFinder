const {MongoClient} = require('mongodb');

const url = "mongodb://localhost:27017"
const client = new MongoClient(url);
const users = new Map()
module.exports = {
	
	getRoom : async (user_id, callback) => {
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


	addPayload:  async (payload) => {
		await client.connect();
		let db = await client.db("ucmfinder");
		let chats = await db.collection("chats");
		await chats.insertOne(payload).catch(err => {
			console.error(err);
		})
		await client.close();
	},

	getChatData : async (room_id, callback) => {
		
		await client.connect();
		let db = await client.db("ucmfinder");
		let chats = await db.collection("chats");
		await chats.find({room_id: room_id}, function (err, result) {
			if (err) throw err
			return callback(result)
		})
		
	},

	addUser : (socket_id, room) => {
		users.set(socket_id, room)
	},

	getUser: (socket_id) => {
		return users.get(socket_id);
	},

	removeUser : (socket_id) => {
		users.delete(socket_id);
	}

}




