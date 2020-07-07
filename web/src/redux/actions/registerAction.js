import { register } from '../../api/userAPI'

export const EMAIL_CHANGE = 'register/EMAIL_CHANGE'
export const PASSWORD_CHANGE = 'register/PASSWORD_CHANGE'
export const CONFIRM_PASSWORD_CHANGE = 'register/CONFIRM_PASSWORD_CHANGE'
export const REGISTER_CLICK = 'register/REGISTER_CLICK'
export const REGISTERING = 'register/REGISTERING'
export const REGISTERED = 'register/REGISTERED'
export const EMAIL_EXIST = 'register/EMAIL_EXIST'
export const PASSWORD_NOT_MATCH = 'register/PASSWORD_NOT_MATCH'
export const REGISTER_FAILED = 'register/REGISTER_FAILED'
export const CLOSE_MODAL_AND_REDIRECT = 'register/CLOSE_MODAL_AND_REDIRECT'
export const CLOSE_MODAL = 'register/CLOSE_MODAL'

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

export const onConfirmPasswordChanged = (password) => dispatch => {
    dispatch({
        type: CONFIRM_PASSWORD_CHANGE,
        payload: password
    })
}

export const onRegisterClicked = () => (dispatch, getState) => {
    const email = getState().register.email
    const password = getState().register.password
    const confirmPassword = getState().register.confirmPassword
    dispatch({ type: REGISTER_CLICK })
    dispatch({ type: REGISTERING })
    if(password !== confirmPassword) {
        dispatch({ type: PASSWORD_NOT_MATCH })
    }
    else {
        register(email, password).then((result => {
            if(result.statusCode === 201) {
                localStorage.setItem("token", result.message)
                dispatch({ 
                    type: REGISTERED,
                    payload: "Register successfully" 
                })
                window.location.href = "/"
            }
            else if(result.statusCode === 400) {
                dispatch({ 
                    type: EMAIL_EXIST, 
                    payload: result.message 
                })
            }
            else {
                dispatch({
                    type: REGISTER_FAILED,
                    payload: "Something went wrong, please try again."
                })
            }
        }))
    }
}