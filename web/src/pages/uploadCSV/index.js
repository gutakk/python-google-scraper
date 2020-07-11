import React, { Component } from 'react';
import { connect } from 'react-redux'

import "./style.scss"
import { 
    onUpload,
    fetchCSVAction
} from '../../redux/actions/uploadCSVAction'


class UploadCSV extends Component {
    componentDidMount() {
        this.props.fetchCSVAction()
    }

    render() {
        const { 
            onUpload,
            fetchCSVAction,
            csvList,
            isFetching
        } = this.props
        return (
            <div id="upload-csv-container" className="d-flex flex-column align-items-center">
                <div className="custom-file">
                    <input type="file" className="custom-file-input" id="customFile" onChange={onUpload}/>
                    <label className="custom-file-label">Choose file</label>
                </div>
                <div id="refresh-btn-container"><button className="btn btn-primary" onClick={fetchCSVAction}>Refresh</button></div>
                {
                    isFetching ?
                    <div className="spinner"><i className="fa fa-circle-o-notch fa-spin display-1"></i></div>
                    :
                    <table className="table table-bordered">
                        <thead>
                            <tr className="text-center">
                            <th scope="col">Status</th>
                            <th scope="col">File name</th>
                            <th scope="col">Keywords    </th>
                            <th scope="col">Uploaded</th>
                            </tr>
                        </thead>
                        <tbody>
                            {csvList.map(csv => {
                                return (
                                    <tr key={csv.fileId} className="text-center">
                                        <td>
                                            {
                                                csv.status ?
                                                <a href={`/data-report/${csv.fileId}`}>
                                                    <button><i className="fa fa-eye"></i></button>
                                                </a>
                                                :
                                                <button className="btn btn-primary" disabled>PROCESSING</button>
                                            }
                                        </td>
                                        <td>{csv.filename}</td>
                                        <td>{csv.keywords}</td>
                                        <td>{csv.created}</td>
                                    </tr>
                                )
                            })}
                        </tbody>
                    </table>
                }
            </div>
        )
    }
}

const mapStateToProps = state => ({
    csvList: state.uploadCSV.csvList,
    isFetching: state.uploadCSV.isFetching
})
  
const mapDispatchToProps = dispatch => ({
    onUpload: (e) => dispatch(onUpload(e.target.files[0])),
    fetchCSVAction: () => dispatch(fetchCSVAction()),
})
  
export default connect(mapStateToProps, mapDispatchToProps)(UploadCSV)
