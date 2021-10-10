import React from 'react'

interface SignupMentorProps {

}

class SignupMentor extends React.Component<SignupMentorProps> {

render () {

	return (
		<div>
			<h1>Signup</h1>
			<p>Name</p>
			<input type="text" name="name" placeholder="Name" />
			<p>About You or Your Family</p>
			<textarea name="" />
			<p>Countries You are looking for</p>
			<input type="text" />
			<p>
			Interests
			</p>
			<textarea name="interests" placeholder="Interest" />
			<h3>Languages</h3>
			<input type="text" placeholder="Languages"/>
			
		</div>
)};
}

export default SignupMentor