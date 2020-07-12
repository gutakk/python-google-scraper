import loginReducer from '../../src/redux/reducers/loginReducer'
import * as actions from '../../src/redux/actions/loginAction'

describe('EMAIL_CHANGE', () => {
    test('returns the correct state', () => {
        const action = { type: actions.EMAIL_CHANGE, payload: "test@email.com" }
        const expectedState = { 
            email: "test@email.com" ,
            password: "",
            emailNotExist: "",
            loginFailedMsg: ""
        }
        expect(loginReducer(undefined, action)).toEqual(expectedState)
    })
})

describe('EMAIL_NOT_EXIST', () => {
    test('returns the correct state', () => {
        const action = { type: actions.EMAIL_NOT_EXIST, payload: "Email not found" }
        const expectedState = { 
            email: "" ,
            password: "",
            emailNotExist: "Email not found",
            loginFailedMsg: ""
        }
        expect(loginReducer(undefined, action)).toEqual(expectedState)
    })
})

describe('LOGIN_CLICK', () => {
    test('returns the correct state', () => {
        const action = { type: actions.LOGIN_CLICK }
        const expectedState = { 
            email: "" ,
            password: "",
            emailNotExist: "",
            loginFailedMsg: ""
        }
        expect(loginReducer(undefined, action)).toEqual(expectedState)
    })
})

describe('LOGIN_FAILED', () => {
    test('returns the correct state', () => {
        const action = { type: actions.LOGIN_FAILED, payload: "Something went wrong" }
        const expectedState = { 
            email: "" ,
            password: "",
            emailNotExist: "",
            loginFailedMsg: "Something went wrong"
        }
        expect(loginReducer(undefined, action)).toEqual(expectedState)
    })
})