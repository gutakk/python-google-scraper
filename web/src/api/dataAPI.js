async function uploadKeywords(keywords) {
    const hostname = window.location.hostname
    const url = "http://" + hostname + ":5000/test-celery"
    const body = {
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

export {
    uploadKeywords
}