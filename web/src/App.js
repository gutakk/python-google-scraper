import { Redirect, Route, Switch } from 'react-router-dom'
import React from 'react';

import Login from './pages/login'
import Register from './pages/register'


function App() {
  const token = localStorage.getItem('token')
  return (
    <div className="App">
      <Switch>
          <Route path='/register'>{token ? <Redirect to=''/> : <Register/>}</Route>
          <Route path='/login'>{token ? <Redirect to=''/> : <Login/>}</Route>
          <Route path='/'><Login/></Route>
          <Redirect from='*' to='/' />
      </Switch>
    </div>
  );
}

export default App;
