CREATE DATABASE OnlineStoreDB;
USE OnlineStoreDB;

-- TABLE CREATION

CREATE TABLE Customers (
    cust_id INT PRIMARY KEY,
    cust_name VARCHAR(100) NOT NULL,
    city VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE
);

CREATE TABLE Products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    price DECIMAL(10 , 2 ) NOT NULL CHECK (price > 0)
);

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    cust_id INT,
    order_date DATE NOT NULL,
    total_amount DECIMAL(10,2),
    FOREIGN KEY (cust_id) REFERENCES Customers(cust_id)
);

CREATE TABLE OrderItems (
    order_item_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT NOT NULL CHECK (quantity > 0),
    item_price DECIMAL(10,2) NOT NULL CHECK (item_price > 0),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);


-- INSERT DATA

INSERT INTO Customers VALUES
(1, 'Prasad', 'Pune', 'prasad@gmail.com'),
(2, 'Amit', 'Mumbai', 'amit@gmail.com'),
(3, 'Sneha', 'Pune', 'sneha@gmail.com'),
(4, 'Rohit', 'Delhi', 'rohit@gmail.com'),
(5, 'Neha', 'Bangalore', 'neha@gmail.com');

INSERT INTO Products VALUES
(101, 'Laptop', 60000),
(102, 'Mobile', 20000),
(103, 'Headphones', 1500),
(104, 'Keyboard', 800),
(105, 'Mouse', 500),
(106, 'Monitor', 12000);

INSERT INTO Orders VALUES
(1, 1, CURRENT_DATE, 62000),
(2, 2, CURRENT_DATE, 20000),
(3, 3, CURRENT_DATE, 1500),
(4, 1, CURRENT_DATE, 12000),
(5, 4, CURRENT_DATE, 800);

INSERT INTO OrderItems VALUES
(1, 1, 101, 1, 60000),
(2, 1, 105, 2, 1000),
(3, 2, 102, 1, 20000),
(4, 3, 103, 1, 1500),
(5, 4, 106, 1, 12000),
(6, 5, 104, 1, 800),
(7, 1, 103, 1, 1500),
(8, 2, 105, 2, 1000),
(9, 3, 105, 1, 500),
(10, 4, 102, 1, 20000);


-- BASIC QUERIES


-- Q3
SELECT * FROM Customers;
SELECT * FROM Products;
SELECT * FROM Orders;
SELECT * FROM OrderItems;

-- Q4
SELECT * FROM Customers WHERE city = 'Pune';

-- Q5
SELECT * FROM Products WHERE price > 1000;


-- JOINS & CLAUSES


-- Q6
SELECT c.cust_name, o.order_id, o.order_date
FROM Customers c
INNER JOIN Orders o ON c.cust_id = o.cust_id;

-- Q7
SELECT o.order_id, p.product_name, oi.quantity
FROM OrderItems oi
JOIN Orders o ON oi.order_id = o.order_id
JOIN Products p ON oi.product_id = p.product_id;

-- Q8
SELECT p.product_name, SUM(oi.quantity * oi.item_price) AS total_sales
FROM OrderItems oi
JOIN Products p ON oi.product_id = p.product_id
GROUP BY p.product_name;

-- Q9
SELECT c.cust_name, SUM(o.total_amount) AS total_spent
FROM Customers c
JOIN Orders o ON c.cust_id = o.cust_id
GROUP BY c.cust_name
HAVING SUM(o.total_amount) > 10000;

-- Q10
SELECT * FROM Products
ORDER BY price DESC
LIMIT 3;

-- ==============================
-- ADVANCED SQL
-- ==============================

-- Q11
SELECT c.cust_name
FROM Customers c
LEFT JOIN Orders o ON c.cust_id = o.cust_id
WHERE o.order_id IS NULL;

-- Q12
SELECT *
FROM Products
WHERE price > (SELECT AVG(price) FROM Products);

-- Q13
SELECT c.city, SUM(o.total_amount) AS total_sales
FROM Customers c
JOIN Orders o ON c.cust_id = o.cust_id
GROUP BY c.city;

-- Q14
SELECT *
FROM Orders
ORDER BY total_amount DESC
LIMIT 1;

-- Q15
SELECT *
FROM Orders
WHERE order_date >= CURRENT_DATE - INTERVAL 30 DAY;