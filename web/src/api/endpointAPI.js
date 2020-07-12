async function fetchEndpoints() {
    const url = `${process.env.REACT_APP_BACKEND_HOST}:${process.env.REACT_APP_BACKEND_PORT}/`
    const response = await fetch(url)
    const data = await response.json()
    return data
}

export {
    fetchEndpoints
}