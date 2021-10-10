import React, {useEffect, useState} from 'react'
import axios from 'axios'
import {useHistory} from "react-router-dom";

interface DashboardProps {

}

const Dashboard: React.FC<DashboardProps> = () => {
	
	const [status, setStatus] = useState<string | null>();
	const [migrants, setMigrants] = useState<Array<any>>();
	const [mentorId, setMentorId] = useState<string | null>();
	const history = useHistory();

	useEffect(() => {
		setStatus(localStorage.getItem("status"));
		setMentorId(localStorage.getItem("id"))
		
			axios.get(`http://127.0.0.1:5000/get-migrants/${localStorage.getItem("id")}`).then((response:any) => {
				setMigrants(response.data.map((data:any) => {
					return <li onClick={() => selectMigrant(data._id)}>
						<h3>{data.name}</h3>
						<p>{data.description}</p>
						<p>{data.languages.map((data:any) => {
							return <li>{data}</li>
						})}</p>
					</li>
				}))	
			})
		
	}, [])

	const selectMigrant = (id:string) => {
		axios.post(`http://127.0.0.1:5000/select-migrant/${mentorId}/${id}`).then((response:any) => {
			localStorage.setItem("room", response.data.room);
			localStorage.setItem("match_id", id);
			history.push("/chat");
		})
	}
		return (<div>
			<h1>Dashboard</h1>
			<ul>{migrants?.length === 0? "There are no migrants avaliable": migrants}</ul>
		</div>);
}

export default Dashboard