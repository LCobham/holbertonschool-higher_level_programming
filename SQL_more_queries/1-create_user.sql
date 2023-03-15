-- Create User user_0d_1 with password user_0d_1_pwd
-- if it doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' 
    IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;