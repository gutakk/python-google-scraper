import { uploadKeywords, fetchCSV } from '../../api/dataAPI'

export const CSV_FETCHED = 'uploadCSV/CSV_FETCHED'
export const CSV_FETCHED_NOT_FOUND = 'uploadCSV/CSV_FETCHED_NOT_FOUND'
export const FETCHING_CSV = 'uploadCSV/FETCHING_CSV'
export const UPLOADING = 'uploadCSV/UPLOADING'
export const UPLOADED = 'uploadCSV/UPLOADED'
export const UNAUTHORIZED = 'uploadCSV/UNAUTHORIZED'
export const UPLOAD_FAILED = 'uploadCSV/UPLOAD_FAILED'
export const CLOSE_UPLOAD_FAILED_MODAL = 'uploadCSV/CLOSE_UPLOAD_FAILED_MODAL'

export const onUpload = (file) => (dispatch, getState) => {
    const endpoints = getState().app.endpoints
    dispatch({ type: UPLOADING })

    let fr = new FileReader()
        fr.onload = (e) => {
            const keywords = (e.target.result).replace(/\n/g, ",").split(",")
            const noEmptyValueKeywords = (keywords.filter(keyword => keyword.length > 0))
            const noDuplicateKeywords = noEmptyValueKeywords.filter((keyword, index) => noEmptyValueKeywords.indexOf(keyword) === index)
            if (noDuplicateKeywords.length > 100) {
                dispatch({ type: UPLOAD_FAILED })
            }
            else {
                uploadKeywords(endpoints["process_csv"], file.name, noDuplicateKeywords).then((result => {
                    if(result.statusCode === 200) {
                        dispatch({ type: UPLOADED })
                        dispatch(fetchCSVAction())
                    }
                    else if(result.statusCode === 401) {
                        removeTokenWhenUnauthorized(dispatch)
                    }
                }))
            }
        }
        fr.readAsText(file)
}

export const fetchCSVAction = () => (dispatch, getState) => {
    const endpoints = getState().app.endpoints
    dispatch({ 
        type: FETCHING_CSV,
        payload: true
     })
    fetchCSV(endpoints["process_csv"]).then(result => {
        if(result.statusCode === 200) {
            let csvList = []
            result["data"].map(csv => {
                csvList.push({
                    fileId: csv[0],
                    filename: csv[1],
                    keywords: csv[2],
                    created: csv[3],
                    status: csv[4]
                })
            })
            dispatch({
                type: CSV_FETCHED,
                payload: csvList
            })
        }
        else if(result.statusCode === 401) {
            removeTokenWhenUnauthorized(dispatch)
        }
        else if(result.statusCode === 404) {
            dispatch({
                type: CSV_FETCHED_NOT_FOUND
            })
        }
    })
}

const removeTokenWhenUnauthorized = (dispatch) => {
    dispatch({ type: UNAUTHORIZED })
    localStorage.removeItem('token')
    window.location.href = "/login"
}

export const closeMoreThan100KWModal = () => dispatch => {
    dispatch({ type: CLOSE_UPLOAD_FAILED_MODAL })
}