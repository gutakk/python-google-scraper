async function register(email, password) {
    const hostname = window.location.hostname
    const url = "http://" + hostname + ":5000/user"
    const body = {
        email: email,
        password: password
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

async function login(email, password) {
    const hostname = window.location.hostname
    const url = "http://" + hostname + ":5000/login"
    const body = {
        email: email,
        password: password
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
    register,
    login
}