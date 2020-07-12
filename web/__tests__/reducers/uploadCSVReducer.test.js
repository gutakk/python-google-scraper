import uploadCSVReducer from '../../src/redux/reducers/uploadCSVReducer'
import * as actions from '../../src/redux/actions/uploadCSVAction'

describe('CSV_FETCHED', () => {
    test('returns the correct state', () => {
        const action = { type: actions.CSV_FETCHED, payload: [1, 2, 3, 4] }
        const expectedState = { 
            csvList: [1, 2, 3, 4],
            isFetching: false
        }
        expect(uploadCSVReducer(undefined, action)).toEqual(expectedState)
    })
})

describe('FETCHING_CSV', () => {
    test('returns the correct state', () => {
        const action = { type: actions.FETCHING_CSV }
        const expectedState = { 
            csvList: [],
            isFetching: true
        }
        expect(uploadCSVReducer(undefined, action)).toEqual(expectedState)
    })
})