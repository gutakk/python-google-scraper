import { Redirect, Route, Switch } from 'react-router-dom'
import { connect } from 'react-redux'
import React from 'react';

import DataReport from './pages/dataReport'
import Login from './pages/login'
import Register from './pages/register'
import UploadCSV from './pages/uploadCSV'
import { 
    fetchEndpoint
} from './redux/actions/appAction'


class App extends React.Component {
    componentDidMount() {
        this.props.fetchEndpoint()
    }

    render() {
        const token = localStorage.getItem('token')
        return (
            <div className="App">
                <Switch>
                    <Route path='/register'>{!token ? <Register/> : <Redirect to=''/> }</Route>
                    <Route path='/login'>{!token ? <Login/> : <Redirect to=''/>}</Route>
                    <Route path='/data-report'><DataReport/></Route>
                    <Route path='/'><UploadCSV/></Route>
                    <Redirect from='*' to='/' />
                </Switch>
            </div>
        )
    }
}

const mapStateToProps = state => ({
    endpoints: state.app.endpoints
})
  
const mapDispatchToProps = dispatch => ({
    fetchEndpoint: () => dispatch(fetchEndpoint()),
})
  
export default connect(mapStateToProps, mapDispatchToProps)(App)
