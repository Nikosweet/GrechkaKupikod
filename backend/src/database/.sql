CREATE DATABASE Pisdata;

CREATE TABLE person(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    hashpassword VARCHAR(72),
    email VARCHAR(50),
    phone VARCHAR(15)
);