-- This script creates a database and a table into it

-- Create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use database
USE hbtn_0d_usa;

-- Create table in database
CREATE TABLE IF NOT EXISTS cities(
	id			INT AUTO_INCREMENT PRIMARY KEY,
	state_id	INT NOT NULL,
	name		VARCHAR(256),
	UNIQUE KEY (id),
	FOREIGN KEY (state_id) REFERENCES states(id)
)
