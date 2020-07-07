import { EMAIL_CHANGE, PASSWORD_CHANGE, EMAIL_NOT_EXIST, LOGIN_CLICK , LOGIN_FAILED } from '../actions/loginAction'
  
export default (state = { 
    email: "",
    password: "",
    emailNotExist: "",
    loginFailedMsg: ""
}, action) => {
    switch (action.type) {
        case EMAIL_CHANGE:
            return {
                ...state,
                email: action.payload
            }
        case PASSWORD_CHANGE:
            return {
                ...state,
                password: action.payload
            }
        case EMAIL_NOT_EXIST:
            return {
                ...state,
                emailNotExist: action.payload
            }
        case LOGIN_CLICK:
            return {
                ...state,
                emailNotExist: ""
            }
        case LOGIN_FAILED:
            return {
                ...state,
                loginFailedMsg: action.payload
            }
        default:
            return state
    }
}