-- 1. Root user
-- Creates the MySQL server user user_0d_1 and grants all privileges to it.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
ALTER USER 'user_0d_1'@'localhost' IDENTIFIED BY 'New-Password-Here';
GRANT ALL PRIVILEGES ON mysql.* TO 'user_0d_1'@'localhost';
