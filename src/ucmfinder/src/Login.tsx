import React, {useState} from 'react'
import axios from 'axios';
import { useHistory } from "react-router-dom";

interface LoginProps {

}

const Login: React.FC<LoginProps> = () => {
	const [username, setUsername] = useState<string>();
	const [password, setPassword] = useState<string>();
	let history = useHistory();
	const submitData = () => {
		axios.post("http://127.0.0.1:5000/create-user", {
			username: username,
			password: password,
		}).then(response => {
			history.push("/dashboard");
		}).catch(err => {

		})
	}
	
		return (<div>
			<h1>Login</h1>
			<p>Username</p>
			<input type="text" placeholder="username" value={username} onChange={(data:any) => setUsername(data)}/>
			<p>Password</p>
			<input type="password" placeholder="password"  value={password} onChange={(data:any) => setPassword(data)}/>
			<input type="submit" value="Submit" onSubmit={submitData}/>
		</div>);
}
export default Login