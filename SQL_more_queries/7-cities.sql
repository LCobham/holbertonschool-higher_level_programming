-- Create database hbtn_0d_usa if it doesn't exist
-- and create table cities in that database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    FOREIGN KEY (state_id)
    REFERENCES states(id),
    name VARCHAR(256) NOT NULL
);