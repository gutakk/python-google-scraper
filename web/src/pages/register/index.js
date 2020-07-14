import React, { Component } from 'react';
import { connect } from 'react-redux'

import "./style.scss"
import { 
    onEmailChanged, 
    onPasswordChanged, 
    onConfirmPasswordChanged, 
    onRegisterClicked
} from '../../redux/actions/registerAction'
import Header from '../../components/header'

class Register extends Component {
    render() {
        const { 
            onEmailChanged, 
            onPasswordChanged, 
            onConfirmPasswordChanged,
            onRegisterClicked,
            email, 
            password,
            confirmPassword,
            isPasswordMatch,
            emailExist,
            registerFailedMsg
        } = this.props
        return (
            <div>
                <Header showLoginLogoutButton={false} showBackButton={true} backPath="/login"/>
                <div id="register-container" className="d-flex align-items-center flex-column">
                    <h2>Register</h2>
                    <form onSubmit={(e) => {e.preventDefault(); onRegisterClicked()}}>
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
                        <div className="form-group">
                            <label>Confirm Password</label>
                            <input 
                                type="password" 
                                className="form-control" 
                                id="exampleInputPassword1"
                                onChange={onConfirmPasswordChanged}
                                required/>
                        </div>
                        <div id="register-error-msg-container" className="text-center text-danger font-weight-bold">
                            { !isPasswordMatch && <p id="register-password-not-match" className="register-error-msg">Password not match</p>}
                            { emailExist && <p id="register-email-exist" className="register-error-msg">{emailExist}</p>}
                            { registerFailedMsg && <p id="register-email-exist" className="register-error-msg">{registerFailedMsg}</p>}
                        </div>
                        <div className="text-center">
                            <button 
                                type="submit" 
                                className="btn btn-primary"
                                disabled={!email || !password || !confirmPassword}>
                                    Register
                            </button>
                        </div>
                    </form>
                </div>
            </div>
        )
    }
}

const mapStateToProps = state => ({
    email: state.register.email,
    password: state.register.password,
    confirmPassword: state.register.confirmPassword,
    isPasswordMatch: state.register.isPasswordMatch,
    emailExist: state.register.emailExist,
    registerFailedMsg: state.register.registerFailedMsg
})
  
const mapDispatchToProps = dispatch => ({
    onEmailChanged: (e) => dispatch(onEmailChanged(e.target.value)),
    onPasswordChanged: (e) => dispatch(onPasswordChanged(e.target.value)),
    onConfirmPasswordChanged: (e) => dispatch(onConfirmPasswordChanged(e.target.value)),
    onRegisterClicked: () => dispatch(onRegisterClicked())
})
  
export default connect(mapStateToProps, mapDispatchToProps)(Register)
