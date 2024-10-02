CREATE DATABASE IF NOT EXISTS latch;

USE latch;

CREATE TABLE IF NOT EXISTS latch (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    operation_id VARCHAR(255) NOT NULL,
    operation_name VARCHAR(255) NOT NULL,
    latch ENUM('on', 'off') NOT NULL
);

CREATE USER IF NOT EXISTS 'latch'@'%' IDENTIFIED BY 'latch';

GRANT ALL ON latch.* TO 'latch'@'%';

GRANT SELECT ON latch.latch TO '$wordpress_user'@'%';

FLUSH PRIVILEGES;