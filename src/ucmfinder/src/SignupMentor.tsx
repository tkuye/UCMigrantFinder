import React,{useState} from 'react'
import axios from 'axios';
import {useHistory} from "react-router-dom";
interface SignupMentorProps {

}

const SignupMentor: React.FC<SignupMentorProps> = () => {
	let history = useHistory();
	const [username, setUsername] = useState<string>();
	const [password, setPassword] = useState<string>();
	const [name, setName] = useState<string>();
	const [aboutYou, setAboutYou] = useState<string>();
	const [country, setCountry] = useState<string>();
	const [interests, setInterests] = useState<string>();
	const [language, setLanguage] = useState<string>();
	const [location, setLocation] = useState<Array<any>>();

	const success = (pos:any) => {
		let crd = pos.coords;
		setLocation([crd.latitude, crd.longitude]);
	}
	const error = (pos:any) => {
		setLocation([0.00, 0.000])
	}

	const submitData = () => {
		axios.post("http://127.0.0.1:5000/create-user", {
			username: username,
			password: password,
		}).then(response => {
			let langs = language?.split(" ");
			let inters = interests?.split(" ");

			navigator.geolocation.getCurrentPosition(success, error)
			let data = {
				country,
				name,
				description:aboutYou,
				languages: langs,
				interests: inters,
				demographics:{},
				match:"none",
				location,
			}
			axios.post("http://127.0.0.1:5000/new-mentor", data).then((res:any) => {
				localStorage.setItem("id", res.data.id);
				localStorage.setItem("status", "mentor");
				history.push("/home-mentors");
			})
		})
	}


	return (
		<div>
			<h1>Signup For Mentors</h1>
			<p>Username</p>
			<input type="text" placeholder="username" value={username} onChange={(data) => setUsername(data.target.value)}/>
			<p>Password</p>
			<input type="password" placeholder="password"  value={password} onChange={(data:any) => setPassword(data.target.value)}/>
			<p>Name</p>
			<input type="text" name="name" placeholder="Name" value={name} onChange={(data:any) => setName(data.target.value)}/>
			<p>About You</p>
			<textarea name="" value={aboutYou} onChange={(data:any) => setAboutYou(data.target.value)}/>
			<p>Current Country</p>
			<input type="text" value={country} placeholder="Country" onChange={(data:any) => setCountry(data.target.value)}/>
			<p>
			Interests
			</p>
			<textarea name="interests" placeholder="Interest" value={interests} onChange={(data:any) => setInterests(data.target.value)}/>
			<h3>Languages</h3>
			<input type="text" placeholder="Languages" value={language} onChange={(data:any) => setLanguage(data.target.value)}/>
			<input type="submit" value="Submit" onClick={submitData}/>
		</div>
	)

}

export default SignupMentor