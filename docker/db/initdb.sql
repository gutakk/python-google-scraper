CREATE EXTENSION pgcrypto;
CREATE EXTENSION "uuid-ossp";

CREATE TABLE users (
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    PRIMARY KEY(email)
);

CREATE TABLE file (
    file_id TEXT NOT NULL,
    filename TEXT NOT NULL,
    keywords INT NOT NULL,
    created TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    PRIMARY KEY(file_id)
);

CREATE TABLE data (
    file_id TEXT NOT NULL REFERENCES file(file_id),
    keyword TEXT NOT NULL,
    total_adword INT,
    total_link INT,
    total_search_result TEXT,
    html_code TEXT,
    created TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    PRIMARY KEY(file_id)
);

CREATE INDEX ON users (email, password);
CREATE INDEX ON file (created);
CREATE INDEX ON data (keyword);