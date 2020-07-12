import configureStore from 'redux-mock-store';
import thunk from 'redux-thunk'
import * as actions from '../../src/redux/actions/registerAction'
import fetchMock, { mock } from 'fetch-mock'

const middlewares = [thunk]
const mockStore = configureStore(middlewares);
let store = mockStore();


describe("clear action", () => {
    beforeEach(() => { // Runs before each test in the suite
        store.clearActions();
    })

    describe("email change", () => {
        test("Dispatches the correct action and payload", () => {
            const expectedActions = [
                {
                    "payload": "test@email.com",
                    "type": "register/EMAIL_CHANGE",
                }
            ]
            store.dispatch(actions.onEmailChanged("test@email.com"));
            expect(store.getActions()).toEqual(expectedActions);
        })
    })

    describe("password change", () => {
        test("Dispatches the correct action and payload", () => {
            const expectedActions = [
                {
                    "payload": "1234",
                    "type": "register/PASSWORD_CHANGE",
                }
            ]
            store.dispatch(actions.onPasswordChanged("1234"));
            expect(store.getActions()).toEqual(expectedActions);
        })
    })

    describe("confirm password change", () => {
        test("Dispatches the correct action and payload", () => {
            const expectedActions = [
                {
                    "payload": "1234",
                    "type": "register/CONFIRM_PASSWORD_CHANGE",
                }
            ]
            store.dispatch(actions.onConfirmPasswordChanged("1234"));
            expect(store.getActions()).toEqual(expectedActions);
        })
    })

    describe("register click", () => {
        test("Password and Confirm password not match", () => {
            
            const expectedActions = [
                {"type": "register/REGISTER_CLICK"},
                {"type": "register/REGISTERING"},
                {"type": "register/PASSWORD_NOT_MATCH"}
            ]
            store = mockStore({
                register: {
                    email: "test@email.com",
                    password: "1234",
                    confirmPassword: "123"
                }
            })
            store.dispatch(actions.onRegisterClicked());
            expect(store.getActions()).toEqual(expectedActions);
        })

        test("Password and Confirm password match", () => {
            
            const expectedActions = [
                {"type": "register/REGISTER_CLICK"},
                {"type": "register/REGISTERING"},
                {"type": "register/PASSWORD_NOT_MATCH"}
            ]
            store = mockStore({
                register: {
                    email: "test@email.com",
                    password: "1234",
                    confirmPassword: "1234"
                }
            })
            store.dispatch(actions.onRegisterClicked());
            expect(store.getActions()).toEqual(expectedActions);
        })
    })
})