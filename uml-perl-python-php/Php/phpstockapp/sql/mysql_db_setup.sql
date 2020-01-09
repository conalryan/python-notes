
CREATE DATABASE `phpstockapp`;

CREATE USER 'monty'@'localhost' IDENTIFIED BY 'some_pass';
GRANT SELECT, INSERT, UPDATE ON `phpstockapp`.* TO 'monty'@'localhost';

CREATE TABLE stock_quotes (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    user_name VARCHAR(30) NOT NULL,
    stock_symbol VARCHAR(10) NOT NULL,
    stock_price DECIMAL NOT NULL
)

INSERT INTO stock_quotes (user_name, stock_symbol, stock_price) VALUES('monty', 'AAPL', 123.25);
INSERT INTO stock_quotes (user_name, stock_symbol, stock_price) VALUES('monty', 'BAC', 15.31);
INSERT INTO stock_quotes (user_name, stock_symbol, stock_price) VALUES('monty', 'GOOG', 548.34);
INSERT INTO stock_quotes (user_name, stock_symbol, stock_price) VALUES('monty', 'EBAY', 57.63);