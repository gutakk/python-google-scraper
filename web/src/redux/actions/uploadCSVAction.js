import { uploadKeywords } from '../../api/dataAPI'


export const UPLOAD_CLICK = 'login/UPLOAD_CLICK'
export const UPLOADING = 'login/UPLOADING'
export const UPLOADED = 'login/UPLOADED'

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
            }))
        };
        fr.readAsText(file);
}