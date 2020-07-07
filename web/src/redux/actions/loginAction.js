import { login } from '../../api/userAPI'


export const EMAIL_CHANGE = 'login/EMAIL_CHANGE'
export const PASSWORD_CHANGE = 'login/PASSWORD_CHANGE'
export const LOGIN_CLICK = 'login/LOGIN_CLICK'
export const LOGGING_IN = 'login/LOGGING_IN'
export const LOGGED_IN = 'login/LOGGED_IN'
export const EMAIL_NOT_EXIST = 'login/EMAIL_NOT_EXIST'
export const LOGIN_FAILED = 'login/LOGIN_FAILED'

export const onEmailChanged = (email) => dispatch => {
    dispatch({ 
        type: EMAIL_CHANGE,
        payload: email
    })
}

export const onPasswordChanged = (password) => dispatch => {
    dispatch({
        type: PASSWORD_CHANGE,
        payload: password
    })
}

export const onLoginClicked = () => (dispatch, getState) => {
    const email = getState().login.email
    const password = getState().login.password
    dispatch({ type: LOGIN_CLICK })
    dispatch({ type: LOGGING_IN })
    
    login(email, password).then((result => {
        if(result.statusCode === 200) {
            localStorage.setItem("token", result.message)
            dispatch({ type: LOGGED_IN })
            window.location.href = "/"
        }
        else if(result.statusCode === 400) {
            dispatch({ 
                type: EMAIL_NOT_EXIST, 
                payload: result.message 
            })
        }
        else {
            dispatch({
                type: LOGIN_FAILED,
                payload: "Something went wrong, please try again."
            })
        }
    }))
}