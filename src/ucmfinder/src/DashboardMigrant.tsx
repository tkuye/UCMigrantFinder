import React, { useEffect, useState} from 'react'
import axios from 'axios';
import {useHistory} from "react-router-dom";
interface DashboardMigrantProps {

}

const DashboardMigrant: React.FC<DashboardMigrantProps> = () => {
	const [mentors, setMentors] = useState<Array<any>>();
	const history = useHistory();

	const selectMentor = (mentor_id:string) => {
		let migrant_id = localStorage.getItem("id");
		
		axios.post(`http://127.0.0.1/5000/select-mentor/${mentor_id}/${migrant_id}`).then((response:any) => {
			localStorage.setItem("room", response.data.room);
			localStorage.setItem("match_id", mentor_id);
			history.push("/chat");
		})
	}	

	useEffect(() => {
		
		axios.get(`http://127.0.0.1/5000/get-matched-mentors/${localStorage.getItem("id")}`).then((response:any) => {
				setMentors(response.data.map((data:any) => {
					return <li onClick={() => selectMentor(data._id)}>
						<h3>{data.name}</h3>
						<p>{data.description}</p>
						<p>{data.languages.map((data:any) => {
							return <li>{data}</li>
						})}</p>
					</li>
				}))	
			})
		
	})
		return (<div>
			<h1>Dashboard</h1>
			{mentors?.length === 0? "You don't have a mentor yet!": mentors}
		</div>);
}
export default DashboardMigrant