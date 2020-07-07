CREATE EXTENSION pgcrypto;
CREATE EXTENSION "uuid-ossp";

CREATE TABLE users (
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    PRIMARY KEY(email)
);