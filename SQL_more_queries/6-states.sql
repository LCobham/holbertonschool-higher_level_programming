-- Create database hbtn_0d_usa ans states table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT NOT NULL UNIQUE AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY(id)
);