import { CSV_FETCHED, FETCHING_CSV } from '../actions/uploadCSVAction'
  
export default (state = {
    csvList: [],
    isFetching: false
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
        default:
            return state
    }
}