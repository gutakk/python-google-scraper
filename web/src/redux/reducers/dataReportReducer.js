import { DATA_REPORT_FETCHED } from '../actions/dataReportAction'
  
export default (state = {
    dataReports: []
}, action) => {
    switch (action.type) {
        case DATA_REPORT_FETCHED:
            return {
                ...state,
                dataReports: action.payload
            }
        default:
            return state
    }
}