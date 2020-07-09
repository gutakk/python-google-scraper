import React, { Component } from 'react';
import { connect } from 'react-redux'

import "./style.scss"
import { 
    onUploadClicked
} from '../../redux/actions/uploadCSVAction'


class UploadCSV extends Component {
    render() {
        const { 
            onUploadClicked
        } = this.props
        return (
            <div id="upload-csv-container">
                <input type="file" onChange={onUploadClicked}/>
            </div>
        )
    }
}

const mapStateToProps = state => ({})
  
const mapDispatchToProps = dispatch => ({
    onUploadClicked: (e) => dispatch(onUploadClicked(e.target.files[0]))
})
  
export default connect(mapStateToProps, mapDispatchToProps)(UploadCSV)
