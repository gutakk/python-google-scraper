
import { combineReducers } from 'redux'
import loginReducer from './loginReducer'
import registerReducer from './registerReducer'
import uploadCSVRedeucer from './uploadCSVReducer'

export default combineReducers({
    login: loginReducer,
    register: registerReducer,
    uploadCSV: uploadCSVRedeucer,
})