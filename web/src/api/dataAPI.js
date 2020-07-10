async function uploadKeywords(filename, keywords) {
    const hostname = window.location.hostname
    const url = "http://" + hostname + ":5000/csv"
    const body = {
        filename: filename,
        keywords: keywords
    }
    const config = {
        headers: {
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

async function fetchCSV() {
    const hostname = window.location.hostname
    const url = "http://" + hostname + ":5000/csv"
    const response = await fetch(url)
    const data = await response.json()
    return data
}

export {
    uploadKeywords,
    fetchCSV
}