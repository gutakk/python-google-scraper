import dataReportReducer from '../../src/redux/reducers/dataReportReducer'
import * as actions from '../../src/redux/actions/dataReportAction'

describe('DATA_REPORT_FETCHED', () => {
    test('returns the correct state', () => {
        const action = { type: actions.DATA_REPORT_FETCHED, payload: [1, 2, 3, 4] }
        const expectedState = { 
            dataReports: [1, 2, 3, 4],
        }
        expect(dataReportReducer(undefined, action)).toEqual(expectedState)
    })
})