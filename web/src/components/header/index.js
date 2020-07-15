import './style.scss'
import React from 'react'
import { Link } from 'react-router-dom'

const Header = ({ showLoginLogoutButton, showBackButton, backPath }) => {
    const handleLogout = (path) => {
        localStorage.removeItem("token")
        window.location.href = "/"
    }

    return (
        <div id="header-container" className="border-bottom d-flex align-items-center justify-content-between">
            {
                showBackButton ? <Link to={backPath}><i className="fa fa-arrow-left " aria-hidden="true"></i></Link> : <div></div>
            }
            <div className="text-right">
                {
                    !localStorage.getItem("token") ?
                    showLoginLogoutButton && <Link to="/login"><button className="btn btn-primary">Login</button></Link>
                    :
                    showLoginLogoutButton && <button className="btn btn-secondary" onClick={() => handleLogout()}>Logout</button>
                }
            </div>
        </div>
    )
}

export default Header