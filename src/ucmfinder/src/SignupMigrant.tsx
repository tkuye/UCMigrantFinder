import React, {useState} from 'react'
import axios from 'axios'
import {useHistory} from "react-router-dom";

interface SignupMigrantProps {

}

const SignupMigrant: React.FC<SignupMigrantProps> = () => {
	let history = useHistory();
	const [username, setUsername] = useState<string>("");
	const [password, setPassword] = useState<string>("");
	const [name, setName] = useState<string>("");
	const [aboutYou, setAboutYou] = useState<string>("");
	const [country, setCountry] = useState<string>("");
	const [interests, setInterests] = useState<string>("");
	const [languages, setLanguages] = useState<string>("");
	const [location, setLocation] = useState<Array<any>>();
	const [status, setStatus] = useState<string>("");
	const success = (pos:any) => {
		let crd = pos.coords;
		setLocation([crd.latitude, crd.longitude]);
	}

const error = (pos:any) => {
		setLocation([0.00, 0.000])
	}

const onChangeValue = (event:any) => {
    setStatus(event.target.value);
  }

	const submitData = () => {
		axios.post("http://127.0.0.1:5000/create-user", {
			username: username,
			password: password,
		}).then(response => {
			let langs = languages?.split(" ");
			let inters = interests?.split(" ");
			let countries = country?.split(" ");
			navigator.geolocation.getCurrentPosition(success, error)
			let data = {
				countries,
				name,
				description:aboutYou,
				languages: langs,
				interests: inters,
				demographics:{},
				match:"none",
				status: status,
				location,
			}
			axios.post("http://127.0.0.1:5000/new-migrant", data).then((res:any) => {
				localStorage.setItem("id", res.data.id);
				localStorage.setItem("status", "migrant");
				history.push("/home-migrants");
			})
		})
	}

	return (
		<div>
			<h1>Signup For New or Potential Migrants</h1>
			<p>Username</p>
			<input type="text" placeholder="username" value={username} onChange={(e) => setUsername(e.target.value)}/>
			<p>Password</p>
			<input type="password" placeholder="password" value={password} onChange={(e) => setPassword(e.target.value)}/>
			<p>Name</p>
			<input type="text" name="name" placeholder="Name" value={name} onChange={(e) => setName(e.target.value)}/>
			<p>About You or Your Family</p>
			<textarea name="" value={aboutYou} onChange={(e) => setAboutYou(e.target.value)}/>
			<p>Countries You are looking for</p>
			<input type="text" value={country} onChange={(e) => setCountry(e.target.value)}/>
			<p>
			Interests
			</p>
			<textarea name="interests" placeholder="Interest" value={interests} onChange={(e:any) => setInterests(e.target.value)}/>
			<h3>Languages</h3>
			<input type="text" placeholder="Languages" value={languages} onChange={(e) => setLanguages(e.target.value)}/>
			<h3>What are you applying as?</h3>
			<div onChange={onChangeValue}>
			<p>Immigrant</p>
			<input type="radio" value="Immigrant" name="status"/>
			<p>Refugee</p>
			<input type="radio" value="Refugee"name="status" />
			<input type="submit" value="Submit" onClick={submitData}/>
			</div>
		</div>
	)
}
export default SignupMigrant