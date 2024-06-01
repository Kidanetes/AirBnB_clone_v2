-- creating a user hbnb_dev
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'Hbnb_dev_pwd(123)';
-- creating a database hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- granting all previleges on hbnb_dev_db to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- granting all previleges on performance_schema to hbnb_dev
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
