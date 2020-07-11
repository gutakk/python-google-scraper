import React, { Component } from 'react';
import { connect } from 'react-redux'

import "./style.scss"
import { 
    onUploadClicked,
    fetchCSVAction
} from '../../redux/actions/uploadCSVAction'


class UploadCSV extends Component {
    componentDidMount() {
        this.props.fetchCSVAction()
    }

    render() {
        const { 
            onUploadClicked,
            csvList
        } = this.props
        return (
            <div id="upload-csv-container">
                <input type="file" onChange={onUploadClicked}/>
                <div id="uploaded-csv-container" className="d-flex justify-content-center">
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
                </div>
            </div>
        )
    }
}

const mapStateToProps = state => ({
    csvList: state.uploadCSV.csvList
})
  
const mapDispatchToProps = dispatch => ({
    onUploadClicked: (e) => dispatch(onUploadClicked(e.target.files[0])),
    fetchCSVAction: () => dispatch(fetchCSVAction())
})
  
export default connect(mapStateToProps, mapDispatchToProps)(UploadCSV)
