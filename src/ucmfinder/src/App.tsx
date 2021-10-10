import React from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

import SignupMigrant from './SignupMigrant';
import SignupMentor from './SignupMentor';
import DashboardMentor from './DashboardMentor';
import DashboardMigrant from './DashboardMigrant';
import Chat from './Chat';
import Login from './Login';

function App() {
  return (
    <div className="App">
      <Router>
      <Switch>
      <Route path="/signup-migrants">
        <SignupMigrant />
        </Route>
      <Route path="/signup-mentors">
      <SignupMentor />
      </Route>
      <Route path="/home-mentors" >
        <DashboardMentor />
      </Route>
      <Route path="/home-migrants" >
        <DashboardMigrant />
      </Route>
      <Route path="/chat">
        <Chat />
      </Route>
      <Route path="/login">
        <Login />
      </Route>
      </Switch>
      <Route exact path="/">
        <Home />
      </Route>
      </Router>
      
    </div>
  );
}

const Home = () => {
  return (<div>
          <h1>
        Are you starting as a Migrant or a Mentor?
      </h1>

      <Link to="signup-migrants">Migrant</Link>
      <br />
      <Link to="signup-mentors">Mentor</Link>
  </div>)
}

export default App;


