async function uploadKeywords(path, filename, keywords) {
    const url = `${process.env.REACT_APP_BACKEND_HOST}:${process.env.REACT_APP_BACKEND_PORT}${path}`
    const body = {
        filename: filename,
        keywords: keywords
    }
    const config = {
        headers: {
            "Authorization": localStorage.getItem('token'),
            "Content-Type": "application/json"
        },
        body: JSON.stringify(body),
        method: "POST"
    }
    const response = await fetch(url, config)
    const statusCode = response.status
    const message = await response.text()
    return {
        message: message,
        statusCode: statusCode
    }
}

async function fetchCSV(path) {
    const url = `${process.env.REACT_APP_BACKEND_HOST}:${process.env.REACT_APP_BACKEND_PORT}${path}`
    const response = await fetch(url)
    const data = await response.json()
    return data
}

async function fetchDataReport(path, fileId) {
    const replacedPath = path.replace("<file_id>", fileId)
    const url = `${process.env.REACT_APP_BACKEND_HOST}:${process.env.REACT_APP_BACKEND_PORT}${replacedPath}`
    const response = await fetch(url)
    const data = await response.json()
    return data
}

export {
    uploadKeywords,
    fetchCSV,
    fetchDataReport
}