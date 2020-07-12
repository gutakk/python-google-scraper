import registerReducer from '../../src/redux/reducers/registerReducer'
import * as actions from '../../src/redux/actions/registerAction'

describe('EMAIL_CHANGE', () => {
    test('returns the correct state', () => {
        const action = { type: actions.EMAIL_CHANGE, payload: "test@email.com" }
        const expectedState = { 
            email: "test@email.com",
            password: "",
            confirmPassword: "",
            isPasswordMatch: true,
            emailExist: "",
            registerFailedMsg: ""
        }
        expect(registerReducer(undefined, action)).toEqual(expectedState)
    })
})

describe('PASSWORD_CHANGE', () => {
    test('returns the correct state', () => {
        const action = { type: actions.PASSWORD_CHANGE, payload: "1234" }
        const expectedState = { 
            email: "",
            password: "1234",
            confirmPassword: "",
            isPasswordMatch: true,
            emailExist: "",
            registerFailedMsg: ""
        }
        expect(registerReducer(undefined, action)).toEqual(expectedState)
    })
})

describe('CONFIRM_PASSWORD_CHANGE', () => {
    test('returns the correct state', () => {
        const action = { type: actions.CONFIRM_PASSWORD_CHANGE, payload: "1234" }
        const expectedState = { 
            email: "",
            password: "",
            confirmPassword: "1234",
            isPasswordMatch: true,
            emailExist: "",
            registerFailedMsg: ""
        }
        expect(registerReducer(undefined, action)).toEqual(expectedState)
    })
})

describe('REGISTER_CLICK', () => {
    test('returns the correct state', () => {
        const action = { type: actions.REGISTER_CLICK }
        const expectedState = { 
            email: "",
            password: "",
            confirmPassword: "",
            isPasswordMatch: true,
            emailExist: "",
            registerFailedMsg: ""
        }
        expect(registerReducer(undefined, action)).toEqual(expectedState)
    })
})

describe('PASSWORD_NOT_MATCH', () => {
    test('returns the correct state', () => {
        const action = { type: actions.PASSWORD_NOT_MATCH }
        const expectedState = { 
            email: "",
            password: "",
            confirmPassword: "",
            isPasswordMatch: false,
            emailExist: "",
            registerFailedMsg: ""
        }
        expect(registerReducer(undefined, action)).toEqual(expectedState)
    })
})

describe('EMAIL_EXIST', () => {
    test('returns the correct state', () => {
        const action = { type: actions.EMAIL_EXIST, payload: "Email Exist" }
        const expectedState = { 
            email: "",
            password: "",
            confirmPassword: "",
            isPasswordMatch: true,
            emailExist: "Email Exist",
            registerFailedMsg: ""
        }
        expect(registerReducer(undefined, action)).toEqual(expectedState)
    })
})

describe('REGISTER_FAILED', () => {
    test('returns the correct state', () => {
        const action = { type: actions.REGISTER_FAILED, payload: "Something went wrong" }
        const expectedState = { 
            email: "",
            password: "",
            confirmPassword: "",
            isPasswordMatch: true,
            emailExist: "",
            registerFailedMsg: "Something went wrong"
        }
        expect(registerReducer(undefined, action)).toEqual(expectedState)
    })
})