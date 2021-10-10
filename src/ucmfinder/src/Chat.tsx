import React, { useEffect, useState } from 'react'
import {io} from "socket.io-client";
import axios from "axios";

const socket = io();

interface ChatProps {

}

const Chat: React.FC<ChatProps> = ({}) => {
	const [chats, setChats] = useState<any>()
	const [chat, setChat] = useState<string>("")


	useEffect(() => {
		axios.get("http://localhost:3001", {
			params:localStorage.getItem("room")
		}).then(result => {
			let data: Array<any> = result.data;
			data.map((data: any) => {
				return <li>
					{data.message}
				</li>
			})
			setChats(data)
		})

		socket.on("connect", () => {
			socket.emit("join", localStorage.getItem("room"));
		})

		socket.on("new-message", message => {
			const converted_message = <li>{message.message}</li>
			setChats((chat:any) => [...chat, converted_message])
		})


	} ,[])

	const submitMessage = () => {
		const message = {
			message: chat,
			time: Date.now(),
			room: localStorage.getItem("room")
		}
		socket.emit("message", message);
	}
		return (<div>
			<ul>
				{chats}
			</ul>
			<input type="text" placeholder="Message" value={chat} onChange={(data:any) => setChat(data)}/>
			<input type="submit" onSubmit ={() => submitMessage()}/>
		</div>);
}
export default Chat