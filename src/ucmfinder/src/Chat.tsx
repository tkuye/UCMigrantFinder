import React, { useEffect, useState } from 'react'
import io from "socket.io-client";
import axios from "axios";

const newSocket = io("http://localhost:3001");


interface ChatProps {

}
const socket = io("");
const Chat: React.FC<ChatProps> = () => {
	const [chats, setChats] = useState<Array<any> | null>(null)
	const [chat, setChat] = useState<string>("")
	const [matchName, setMatchName] = useState<string>("")

	useEffect(() => {
		
		axios.get(`http://localhost:3001/chat-data/`, {
			params:{
				room_id: localStorage.getItem("room")}
		}).then((result:any) => {
			let data: Array<any> = result.data;

			setChats(data.map((d: any) => {
				return (<li>
					{d.message}
				</li>)
			}))
			
		})

		let status = localStorage.getItem("status");
		let match_id = localStorage.getItem("match_id");
		if (status === "migrant"){
			axios.get(`http://127.0.01:5000/get-mentor/${match_id}`).then((result:any) => {
				setMatchName(result.data?.name)
			})
		}
		else if (status === "mentor"){
			axios.get(`http://127.0.01:5000/get-migrant/${match_id}`).then((result:any) => {
				setMatchName(result.data?.name)
			})
		}

		
		newSocket.on("connect", () => {
			newSocket.emit("join", localStorage.getItem("room"));
		})

		newSocket.on("new-message", (message:any) => {
			const converted_message = <li>{message.message}</li>
			setChats((chat:any) => [...chat, converted_message])
		})

	}, [chats, matchName])

	const submitMessage = () => {
		
		const message = {
			message: chat,
			time: Date.now(),
			room: localStorage.getItem("room")
		}
		setChats((chatse:any) => [...chatse, <li>{chat}</li>])
		newSocket.emit("message", message);
	}
		return (<div>
			<h2>{matchName}</h2>
			<ul>
				{chats?.length === 0? "There are no chats to display": chats}
			</ul>
			<input type="text" placeholder="Message" value={chat} onChange={(data:any) => setChat(data.target.value)}/>
			<input type="submit" onClick ={() => submitMessage()}/>
		</div>);
}
export default Chat