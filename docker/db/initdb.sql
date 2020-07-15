CREATE EXTENSION pgcrypto;
CREATE EXTENSION "uuid-ossp";

CREATE TABLE users (
    id SERIAL NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE file (
    user_id INT NOT NULL REFERENCES users(id),
    id SERIAL NOT NULL,
    filename TEXT NOT NULL,
    keywords INT NOT NULL,
    created TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    PRIMARY KEY(id)
);

CREATE TABLE data (
    file_id INT NOT NULL REFERENCES file(id),
    keyword TEXT NOT NULL,
    total_adword INT,
    total_link INT,
    total_search_result TEXT,
    html_code TEXT,
    created TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    PRIMARY KEY(file_id, keyword)
);

CREATE INDEX ON users (email, password);
CREATE INDEX ON file (created);
CREATE INDEX ON file (user_id);
CREATE INDEX ON data (keyword);