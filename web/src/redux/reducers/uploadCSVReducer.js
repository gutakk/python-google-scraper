import { CSV_FETCHED, UPLOAD_CLICK, UPLOADING, UPLOADED } from '../actions/uploadCSVAction'
  
export default (state = {
    csvList: []
}, action) => {
    switch (action.type) {
        case UPLOAD_CLICK:
            return {
                ...state
            }
        case UPLOADING:
            return {
                ...state,
            }
        case UPLOADED:
            return {
                ...state,
            }
        case CSV_FETCHED:
            return {
                ...state,
                csvList: action.payload
            }
        default:
            return state
    }
}