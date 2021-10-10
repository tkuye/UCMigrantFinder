const { createServer } = require('http')
const express = require('express')
const {Server} = require('socket.io');
const {getChatData, removeUser, addUser, addPayload} = require('./users')

const app = express();
const httpServer = createServer(app);
const io = new Server(httpServer , {
	path:"/chat"
})

io.on("connection", (socket) => {
	addUser(socket.id, socket.data.room)
	
	socket.on("join", room => {
		socket.join(room);
	})

	socket.on("disconnect", () => {
	removeUser(socket.id);
})

socket.on("message", (message) => {
	addPayload(message)
	socket.to(getUser(socket.id)).emit("new-message", message)
})
})

app.get("/chat-data", (req, res) => {
	getChatData(req.query.room_id, (result) => {
		res.send(result)
	})
})

httpServer.listen(3001)