-- Create a MySQL server
-- Database hbnb_test_db
-- User hbnb_test with password hbnb_test_pwd in localhost
-- Grant all privileges for hbnb_test on hbnb_test_db
-- Grant SELECT privilege for hbnb_test on performance_schema

-- CREATE database hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- CREATE user hbnb_test
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- GRANT all privileges to hbnb_test on hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- GRANT SELECT privilage to hbnb_test on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- FLUSH so everything gets applies
FLUSH PRIVILEGES;
