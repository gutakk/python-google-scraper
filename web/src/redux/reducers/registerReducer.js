import { 
    EMAIL_CHANGE, 
    PASSWORD_CHANGE, 
    CONFIRM_PASSWORD_CHANGE, 
    REGISTER_CLICK, 
    PASSWORD_NOT_MATCH,
    EMAIL_EXIST,
    REGISTER_FAILED
} from '../actions/registerAction'
  
export default (state = { 
    email: "",
    password: "",
    confirmPassword: "",
    isPasswordMatch: true,
    emailExist: "",
    registerFailedMsg: ""
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
        case CONFIRM_PASSWORD_CHANGE:
            return {
                ...state,
                confirmPassword: action.payload
            }
        case REGISTER_CLICK:
            return {
                ...state,
                isPasswordMatch: true,
                emailExist: "",
                registerFailedMsg: ""
            }
        case PASSWORD_NOT_MATCH:
            return {
                ...state,
                isPasswordMatch: false
            }
        case EMAIL_EXIST:
            return {
                ...state,
                emailExist: action.payload
            }
        case REGISTER_FAILED:
            return {
                ...state,
                registerFailedMsg: action.payload
            }
        default:
            return state
    }
}