import React, { Component } from 'react';
import { connect } from 'react-redux'
import { Link } from 'react-router-dom'

import "./style.scss"
import { 
    onEmailChanged, 
    onPasswordChanged, 
    onLoginClicked
} from '../../redux/actions/loginAction'


class Login extends Component {
    render() {
        const { 
            onEmailChanged, 
            onPasswordChanged, 
            onLoginClicked,
            email, 
            password,
            emailNotExist,
            loginFailedMsg
        } = this.props
        return (
            <div id="login-container" className="d-flex align-items-center flex-column">
                <h2>Login</h2>
                <form onSubmit={(e) => {e.preventDefault(); onLoginClicked()}}>
                    <div className="form-group">
                        <label>Email address</label>
                        <input 
                            type="email" 
                            className="form-control" 
                            id="exampleInputEmail1" 
                            aria-describedby="emailHelp"
                            onChange={onEmailChanged}
                            required/>
                    </div>
                    <div className="form-group">
                        <label>Password</label>
                        <input 
                            type="password" 
                            className="form-control" 
                            id="exampleInputPassword1"
                            onChange={onPasswordChanged}
                            required/>
                    </div>
                    <div id="login-error-msg-container" className="text-center text-danger font-weight-bold">
                        { emailNotExist && <p id="login-email-exist">{emailNotExist}</p>}
                        { loginFailedMsg && <p id="login-email-exist">{loginFailedMsg}</p>}
                    </div>
                    <div className="text-center">
                        <button 
                            type="submit" 
                            className="btn btn-primary"
                            disabled={!email || !password}>
                                Login
                        </button>
                    </div>
                </form>
                <p id="sign-up-content">No account yet? <Link id="sign-up" to="/register" className="font-weight-bold">Sign up for free!</Link></p>
            </div>
        )
    }
}

const mapStateToProps = state => ({
    email: state.login.email,
    password: state.login.password,
    isPasswordMatch: state.login.isPasswordMatch,
    emailNotExist: state.login.emailNotExist,
    loginFailedMsg: state.login.loginFailedMsg
})
  
const mapDispatchToProps = dispatch => ({
    onEmailChanged: (e) => dispatch(onEmailChanged(e.target.value)),
    onPasswordChanged: (e) => dispatch(onPasswordChanged(e.target.value)),
    onLoginClicked: () => dispatch(onLoginClicked())
})
  
export default connect(mapStateToProps, mapDispatchToProps)(Login)
