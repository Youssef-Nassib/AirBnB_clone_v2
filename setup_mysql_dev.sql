--   Creates a MySQL server
--   Database hbnb_dev_db
--   User hbnb_dev with password hbnb_dev_pwd in localhost
--   Grant all privileges for hbnb_dev on hbnb_dev_db
--   Grant SELECT privilege for hbnb_dev on performance

-- CRAETE database hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- CREATE new user hbnb_dev
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- GRANT privileges to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- GARNT SELECT privilege to hbnb_dev on performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- FLUSH so everything gets applied
FLUSH PRIVILEGES;
