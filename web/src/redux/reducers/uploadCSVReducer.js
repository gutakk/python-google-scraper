import { CSV_FETCHED, FETCHING_CSV, UPLOAD_FAILED, CLOSE_UPLOAD_FAILED_MODAL } from '../actions/uploadCSVAction'
  
export default (state = {
    csvList: [],
    isFetching: false,
    csvMoreThan100KW: false
}, action) => {
    switch (action.type) {
        case FETCHING_CSV:
            return {
                ...state,
                isFetching: true
            }
        case CSV_FETCHED:
            return {
                ...state,
                csvList: action.payload,
                isFetching: false
            }
        case UPLOAD_FAILED:
            return {
                ...state,
                csvMoreThan100KW: true
            }
        case CLOSE_UPLOAD_FAILED_MODAL:
            return {
                ...state,
                csvMoreThan100KW: false
            }
        default:
            return state
    }
}