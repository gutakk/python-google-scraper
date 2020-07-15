import React, { Component } from 'react';
import { connect } from 'react-redux'

import "./style.scss"
import {
    fetchDataAction
} from '../../redux/actions/dataReportAction'
import Header from '../../components/header'

class DataReport extends Component {
    componentDidMount() {
        if(!this.props.isFetchingEndpoints)
            this.props.fetchDataAction()
    }

    render() {
        const { dataReports } = this.props
        return (
            <div>
                <Header showLoginLogoutButton={true} showBackButton={true} backPath="/"/>
                <div id="data-report-container" className="d-flex flex-column align-items-center">
                    {
                        dataReports.length > 0 ? 
                        <table className="table table-bordered">
                        <thead>
                            <tr className="text-center">
                            <th scope="col">Keyword</th>
                            <th scope="col">Total Adwords</th>
                            <th scope="col">Total Links</th>
                            <th scope="col">Total Search Results</th>
                            <th scope="col">HTML Code</th>
                            </tr>
                        </thead>
                        <tbody>
                            {dataReports.map(dataReport => {
                                return (
                                    <tr key={dataReport.keyword} className="text-center">
                                        <td>{dataReport.keyword}</td>
                                        <td>{dataReport.totalAdwords}</td>
                                        <td>{dataReport.totalLinks}</td>
                                        <td>{dataReport.totalSearchResults}</td>
                                        <td>
                                            <a target="_blank" href={`${process.env.REACT_APP_BACKEND_HOST}:${process.env.REACT_APP_BACKEND_PORT}/html-code/${dataReport.fileId}/${dataReport.keyword}`}>
                                                <button><i className="fa fa-eye"></i></button>
                                            </a>
                                        </td>
                                    </tr>
                                )
                            })}
                        </tbody>
                    </table>
                    :
                    <h2>Data Not Found</h2>
                    }
                </div>
            </div>
        )
    }
}

const mapStateToProps = state => ({
    dataReports: state.dataReport.dataReports,
    isFetchingEndpoints: state.app.isFetchingEndpoints
})
  
const mapDispatchToProps = dispatch => ({
    fetchDataAction: () => dispatch(fetchDataAction())
})
  
export default connect(mapStateToProps, mapDispatchToProps)(DataReport)
