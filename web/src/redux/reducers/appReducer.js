import { ENDPOINT_FETCHED, FETCHING_ENDPOINTS } from '../actions/appAction'
  
export default (state = {
    endpoints: null,
    isFetchingEndpoints: false
}, action) => {
    switch (action.type) {
        case FETCHING_ENDPOINTS:
            return {
                ...state,
                isFetchingEndpoints: true
            }
        case ENDPOINT_FETCHED:
            return {
                ...state,
                endpoints: action.payload,
                isFetchingEndpoints: false
            }
        default:
            return state
    }
}