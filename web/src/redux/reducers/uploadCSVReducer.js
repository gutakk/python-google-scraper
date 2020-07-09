import { UPLOAD_CLICK, UPLOADING, UPLOADED } from '../actions/uploadCSVAction'
  
export default (state = {}, action) => {
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
        default:
            return state
    }
}