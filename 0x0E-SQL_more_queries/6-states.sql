-- This script creates a database and a table into it

-- Create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use database newly created
USE hbtn_0d_usa;

-- Create table in database
CREATE TABLE IF NOT EXISTS states(
	id		INT AUTO_INCREMENT PRIMARY KEY,
	name	VARCHAR(256),
	UNIQUE KEY id (id)
);
