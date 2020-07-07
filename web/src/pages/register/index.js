import { observer } from 'mobx-react'
import React, { Component } from 'react';

import "./style.scss"


class Register extends Component {
    render() {
        return (
            <div id="register-container" className="d-flex align-items-center flex-column">
                <h2>Register</h2>
                <form onSubmit={(e) => {e.preventDefault()}}>
                    <div className="form-group">
                        <label for="exampleInputEmail1">Email address</label>
                        <input type="email" className="form-control" id="exampleInputEmail1" aria-describedby="emailHelp"/>
                    </div>
                    <div className="form-group">
                        <label for="exampleInputPassword1">Password</label>
                        <input type="password" className="form-control" id="exampleInputPassword1"/>
                    </div>
                    <div className="form-group">
                        <label for="exampleInputPassword1">Confirm Password</label>
                        <input type="password" className="form-control" id="exampleInputPassword1"/>
                    </div>
                    <div className="text-center">
                        <button type="submit" className="btn btn-primary">Register</button>
                    </div>
                </form>
            </div>
        )
    }
}

export default Register
