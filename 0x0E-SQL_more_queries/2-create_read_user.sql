-- This script creates a database and a user and grants it privileges

-- Create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privileges to user on database
GRANT SELECT
ON hbtn_0d_2.*
TO 'user_0d_2'@'localhost' ;
