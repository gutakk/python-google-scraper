import { fetchDataReport } from '../../api/dataAPI'

export const DATA_REPORT_FETCHED = 'dataReport/DATA_REPORT_FETCHED'
export const FETCHING_DATA_REPORT = 'dataReport/FETCHING_DATA_REPORT'


export const fetchDataAction = () => (dispatch, getState) => {
    const endpoints = getState().app.endpoints
    dispatch({ type: FETCHING_DATA_REPORT })
    const fileId = window.location.pathname.split("/")[2]
    fetchDataReport(endpoints["data_report"], fileId).then(result => {
        let dataReports = []
        result.map(data => {
            dataReports.push({
                keyword: data[0],
                totalAdwords: data[1],
                totalLinks: data[2],
                totalSearchResults: data[3],
                fileId: data[4]
            })
        })
        dispatch({
            type: DATA_REPORT_FETCHED,
            payload: dataReports
        })
    })
}