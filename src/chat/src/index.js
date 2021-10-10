const { createServer } = require('http')
const express = require('express')
const {Server} = require('socket.io');
const {getChatData, removeUser, addUser, addPayload, getUser} = require('./users')
var cors = require('cors')
const app = express();
app.use(cors())
const httpServer = createServer(app);
const io = new Server(httpServer , { cors: {
    origin: '*',
    methods: ['GET', 'POST']
  }}
  )

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

app.get("/chat-data", async (req, res) => {
	console.log(req.query.room_id);
	let data = await getChatData(req.query.room_id)
	res.send(data)
})

httpServer.listen(3001)