import uploadCSVReducer from '../../src/redux/reducers/uploadCSVReducer'
import * as actions from '../../src/redux/actions/uploadCSVAction'

describe('CSV_FETCHED', () => {
    test('returns the correct state', () => {
        const action = { type: actions.CSV_FETCHED, payload: [1, 2, 3, 4] }
        const expectedState = { 
            csvList: [1, 2, 3, 4],
            isFetching: false,
            csvMoreThan100KW: false
        }
        expect(uploadCSVReducer(undefined, action)).toEqual(expectedState)
    })
})

describe('FETCHING_CSV', () => {
    test('returns the correct state', () => {
        const action = { type: actions.FETCHING_CSV }
        const expectedState = { 
            csvList: [],
            isFetching: true,
            csvMoreThan100KW: false
        }
        expect(uploadCSVReducer(undefined, action)).toEqual(expectedState)
    })
})

describe('UPLOAD_FAILED', () => {
    test('returns the correct state', () => {
        const action = { type: actions.UPLOAD_FAILED }
        const expectedState = { 
            csvList: [],
            isFetching: true,
            csvMoreThan100KW: true
        }
        expect(uploadCSVReducer(undefined, action)).toEqual(expectedState)
    })
})

describe('CLOSE_UPLOAD_FAILED_MODAL', () => {
    test('returns the correct state', () => {
        const action = { type: actions.CLOSE_UPLOAD_FAILED_MODAL }
        const expectedState = { 
            csvList: [],
            isFetching: true,
            csvMoreThan100KW: false
        }
        expect(uploadCSVReducer(undefined, action)).toEqual(expectedState)
    })
})