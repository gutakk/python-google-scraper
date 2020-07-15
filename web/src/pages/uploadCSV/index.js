import React, { Component } from 'react';
import { connect } from 'react-redux'
import { Link } from 'react-router-dom'
import "./style.scss"
import { 
    onUpload,
    fetchCSVAction,
    closeMoreThan100KWModal
} from '../../redux/actions/uploadCSVAction'
import Header from '../../components/header'

class UploadCSV extends Component {
    componentDidMount() {
        if (!this.props.isFetchingEndpoints && localStorage.getItem("token"))
            this.props.fetchCSVAction()
    }

    render() {
        const { 
            onUpload,
            fetchCSVAction,
            closeMoreThan100KWModal,
            csvList,
            isFetching,
            csvMoreThan100KW
        } = this.props
        return (
            <div>
                <Header showLoginLogoutButton={true} showBackButton={false}/>
                <div id="upload-csv-container">
                    {
                        localStorage.getItem("token") ?
                        <div className="d-flex flex-column align-items-center">
                            <div className="custom-file">
                                <input type="file" className="custom-file-input" id="customFile" onChange={onUpload}/>
                                <label className="custom-file-label">Choose file</label>
                            </div>
                            <div id="refresh-btn-container"><button className="btn btn-primary" onClick={fetchCSVAction}>Refresh</button></div>
                            {
                                isFetching ?
                                <div className="spinner"><i className="fa fa-circle-o-notch fa-spin display-1"></i></div>
                                :
                                csvList.length > 0 ?
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
                                                            <Link to={`/data-report/${csv.fileId}`}>
                                                                <button><i className="fa fa-eye"></i></button>
                                                            </Link>
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
                                :
                                <h2 className="text-muted">NO UPLOADED FILES</h2>
                            }
                            {
                                csvMoreThan100KW &&
                                <div className="modal fade show d-block" tabindex="-1" role="dialog">
                                    <div className="modal-dialog" role="document">
                                        <div className="modal-content">
                                        <div className="modal-header">
                                            <h5 className="modal-title">CSV Contains more than 100 keywords</h5>
                                            <button type="button" className="close" data-dismiss="modal" aria-label="Close" onClick={closeMoreThan100KWModal}>
                                                <span aria-hidden="true">&times;</span>
                                            </button>
                                        </div>
                                        <div className="modal-footer">
                                            <button type="button" className="btn btn-danger" data-dismiss="modal" onClick={closeMoreThan100KWModal}>Close</button>
                                        </div>
                                        </div>
                                    </div>
                                </div>
                            }
                        </div>
                        :
                        <div id="require-login" className="text-center"><h2 className="text-muted">This application requires to login first</h2></div>
                    }
                </div>
            </div>
        )
    }
}

const mapStateToProps = state => ({
    csvList: state.uploadCSV.csvList,
    isFetching: state.uploadCSV.isFetching,
    isFetchingEndpoints: state.app.isFetchingEndpoints,
    csvMoreThan100KW: state.uploadCSV.csvMoreThan100KW
})
  
const mapDispatchToProps = dispatch => ({
    onUpload: (e) => dispatch(onUpload(e.target.files[0])),
    fetchCSVAction: () => dispatch(fetchCSVAction()),
    closeMoreThan100KWModal: () => dispatch(closeMoreThan100KWModal())
})
  
export default connect(mapStateToProps, mapDispatchToProps)(UploadCSV)
