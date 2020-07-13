
import { combineReducers } from 'redux'
import appReducer from './appReducer'
import dataReportReducer from './dataReportReducer'
import loginReducer from './loginReducer'
import registerReducer from './registerReducer'
import uploadCSVRedeucer from './uploadCSVReducer'

export default combineReducers({
    app: appReducer,
    dataReport: dataReportReducer,
    login: loginReducer,
    register: registerReducer,
    uploadCSV: uploadCSVRedeucer,
})