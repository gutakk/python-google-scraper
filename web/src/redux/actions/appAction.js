import { fetchEndpoints } from '../../api/endpointAPI'

export const ENDPOINT_FETCHED = 'app/ENDPOINT_FETCHED'
export const FETCHING_ENDPOINTS = 'app/FETCHING_ENDPOINTS'

export const fetchEndpoint = () => dispatch => {
    dispatch({ 
        type: FETCHING_ENDPOINTS,
        payload: true
     })
     fetchEndpoints().then(result => {
        dispatch({
            type: ENDPOINT_FETCHED,
            payload: result
        })
    })
}