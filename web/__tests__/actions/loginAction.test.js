import configureStore from 'redux-mock-store';
import thunk from 'redux-thunk'
import * as actions from '../../src/redux/actions/loginAction'

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
                    "type": "login/EMAIL_CHANGE",
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
                    "type": "login/PASSWORD_CHANGE",
                }
            ]
            store.dispatch(actions.onPasswordChanged("1234"));
            expect(store.getActions()).toEqual(expectedActions);
        })
    })
})