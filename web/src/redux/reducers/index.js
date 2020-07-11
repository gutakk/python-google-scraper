
import { combineReducers } from 'redux'
import dataReportReducer from './dataReportReducer'
import loginReducer from './loginReducer'
import registerReducer from './registerReducer'
import uploadCSVRedeucer from './uploadCSVReducer'

export default combineReducers({
    dataReport: dataReportReducer,
    login: loginReducer,
    register: registerReducer,
    uploadCSV: uploadCSVRedeucer,
})