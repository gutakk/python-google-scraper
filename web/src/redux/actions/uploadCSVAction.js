import { uploadKeywords, fetchCSV } from '../../api/dataAPI'

export const CSV_FETCHED = 'uploadCSV/CSV_FETCHED'
export const FETCHING_CSV = 'uploadCSV/FETCHING_CSV'
export const UPLOAD_CLICK = 'uploadCSV/UPLOAD_CLICK'
export const UPLOADING = 'uploadCSV/UPLOADING'
export const UPLOADED = 'uploadCSV/UPLOADED'

export const onUploadClicked = (file) => dispatch => {
    dispatch({ type: UPLOAD_CLICK })
    dispatch({ type: UPLOADING })

    let fr = new FileReader();
        fr.onload = (e) => {
            let keywords = (e.target.result).replace(/\n/g, ",").replace(/,,/g, ",").split(",")
            keywords.pop()
            console.log(keywords)
            uploadKeywords(file.name, keywords).then((result => {
                if(result.statusCode === 200) {
                    dispatch({ type: UPLOADED })
                }
                window.location.href = "/csv"
            }))
        };
        fr.readAsText(file);
}

export const fetchCSVAction = () => dispatch => {
    dispatch({ type: FETCHING_CSV })
    fetchCSV().then(result => {
        let csvList = []
        result.map(csv => {
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
    })
}