create database Assignment1

use Assignment1

/* Creating Tables */
CREATE TABLE Customers(
	customer_id INT Primary key,
	first_name VARCHAR(20) NOT NULL,
	last_name VARCHAR(20) NOT NULL,
	dob VARCHAR(20) DEFAULT NULL,
	phone INT NOT NULL
)

INSERT INTO	Customers (customer_id, first_name, last_name, dob, phone)	VALUES	(1001, 'Mark','Mark','22 Jan 89',1234);
INSERT INTO	Customers (customer_id, first_name, last_name, dob, phone)	VALUES	(1002, 'John', 'Maximus', '31 March 79',5678)
INSERT INTO	Customers (customer_id, first_name, last_name, dob, phone)	VALUES	(1003, 'Dio', 'Brando', '12 April 68', 9101)
INSERT INTO	Customers (customer_id, first_name, last_name, dob, phone)	VALUES	(1004, 'Ceaser', 'Zepp', '02 Dec 99', 1213)


CREATE TABLE Product_types(
	product_type_id INT Primary key,
	name VARCHAR(30) NOT NULL
)

INSERT INTO Product_types (product_type_id, name) VALUES (2001, 'Cleaning')
INSERT INTO Product_types (product_type_id, name) VALUES (2002, 'Furniture')
INSERT INTO Product_types (product_type_id, name) VALUES (2003, 'Kitchen')
INSERT INTO Product_types (product_type_id, name) VALUES (2004, 'Sports')

CREATE TABLE Products(
	product_id INT Primary key,
	product_type_id INT NOT NULL,
	name VARCHAR(30) NOT NULL,
	description VARCHAR(30) DEFAULT NULL,
	price INT NOT NULL,
	FOREIGN KEY (product_type_id) REFERENCES Product_types (product_type_id)
)

INSERT INTO Products (product_id, product_type_id, name, price) VALUES (3001,2001,'Detergent',200)
INSERT INTO Products (product_id, product_type_id, name, price) VALUES (3002,2003,'Blender',5000)
INSERT INTO Products (product_id, product_type_id, name, price) VALUES (3003,2004,'Football',900)
INSERT INTO Products (product_id, product_type_id, name, price) VALUES (3004,2002,'Chair',1500)

CREATE TABLE Purchases(
	product_id INT,
	customer_id INT NOT NULL,
	quantity INT NOT NULL,
	FOREIGN KEY (product_id) REFERENCES Products (product_id),
	FOREIGN KEY (customer_id) REFERENCES Customers (customer_id)
)

INSERT INTO Purchases (product_id, customer_id, quantity) VALUES (3001,1003,5)
INSERT INTO Purchases (product_id, customer_id, quantity) VALUES (3004,1004,2)
INSERT INTO Purchases (product_id, customer_id, quantity) VALUES (3002,1002,1)
INSERT INTO Purchases (product_id, customer_id, quantity) VALUES (3004,1003,7)


CREATE TABLE Employees(
	employee_id INT PRIMARY key,
	manager_id INT DEFAULT NULL,
	first_name VARCHAR(20) NOT NULL,
	last_name VARCHAR(20) NOT NULL,
	title VARCHAR(20) DEFAULT NULL,
	salary INT NOT NULL
)

INSERT INTO	Employees (employee_id, manager_id, first_name, last_name, title, salary)	VALUES	(4001,4004,'Mick','Foley','Cashier',12000)
INSERT INTO	Employees (employee_id, manager_id, first_name, last_name, title, salary)	VALUES	(4002,4004,'Joe','Obama','Salesman',10000)
INSERT INTO	Employees (employee_id, manager_id, first_name, last_name, title, salary)	VALUES	(4003,4004,'Gio','Gio','Security',11000)
INSERT INTO	Employees (employee_id, first_name, last_name, title, salary)				VALUES	(4004,'Will','Anthonio','Manager',15000)


select * from Customers
select * from Product_types
select * from Products
select * from Purchases
select * from Employees
/* Creating Tables */



/* 1 */
select first_name,last_name
from Employees
where first_name != last_name

/* 2 */
select CONCAT(Customers.first_name,' ',Customers.last_name) AS 'Customer Name', Purchases.product_id
from Customers
LEFT JOIN Purchases on Customers.customer_id = Purchases.customer_id 
order by first_name

/* 3 */
select CONCAT(Customers.first_name,' ',Customers.last_name) AS 'Customer Name',products.name AS 'Product Name'
from Purchases
Inner JOIN Customers on Customers.customer_id = Purchases.customer_id 
Inner JOIN Products on Purchases.product_id = Products.product_id
order by first_name


/* 4 */
select CONCAT(first_name,' ',last_name) 'Customer', Purchases.product_id,products.name,Purchases.quantity
from Customers,Purchases,Products
where Customers.customer_id = Purchases.customer_id  AND Purchases.product_id = Products.product_id AND Customers.first_name = 'John'

/* 5 */
select * 
from Employees
where title = 'Manager'

/* 6 */
select Product_types.product_type_id AS 'Product Type ID',Product_types.name AS 'Product Type', Products.name AS 'Product Name'
from Product_types,Products
where Product_types.product_type_id = Products.product_type_id

/* 7 */
select COUNT( employee_id ) AS 'Number of Managers'
from Employees
where title = 'Manager'

/* 8 */
select COUNT(Customers.customer_id) AS 'Number of orders',CONCAT(Customers.first_name,' ', Customers.last_name) AS 'Customer Name'
from Customers,Purchases
where Customers.customer_id = Purchases.customer_id
group by Customers.first_name,Customers.last_name
having COUNT(Customers.customer_id) = 2


/* 9 */
select MAX(salary) AS 'Highest Paid',Min(salary) AS 'Lowest Paid',MAX(salary) - Min(salary) AS 'Difference'
from Employees 


/* 10 */
CREATE TABLE PRODUCT(
	product_id INT Primary key,
	name VARCHAR(30) NOT NULL,
	price INT NOT NULL,
	expiry VARCHAR(20) DEFAULT NULL
)

INSERT INTO PRODUCT (product_id, name, price, expiry) VALUES (121,'Chips',100,'02/02/2002')
INSERT INTO PRODUCT (product_id, name, price, expiry) VALUES (571,'Potato',10000,'02/02/2002')

CREATE TABLE Dept(
	dept_id INT PRIMARY KEY,
	dept_name VARCHAR(20) NOT NULL,
	dept_locations VARCHAR(20) DEFAULT NULL,
	dept_manager VARCHAR(20) NOT NULL
)
INSERT INTO Dept (dept_id,dept_name,dept_locations,dept_manager) VALUES (01,'Accounting','1st floor','Jim')
INSERT INTO Dept (dept_id,dept_name,dept_locations,dept_manager) VALUES (02,'Guards','Ground floor','Dwight')

CREATE TABLE Employee(
	employee_id INT PRIMARY key,
	manager_id INT DEFAULT NULL,
	dept_id INT NOT NULL,
	first_name VARCHAR(20) NOT NULL,
	last_name VARCHAR(20) NOT NULL,
	title VARCHAR(20) DEFAULT NULL,
	salary INT NOT NULL
	FOREIGN KEY (dept_id) REFERENCES Dept (dept_id)
)
INSERT INTO	Employee (employee_id, manager_id, dept_id, first_name, last_name, title, salary)	VALUES	(5464,4565,02,'ABC','DEF','Cashier',17000)
INSERT INTO	Employee (employee_id, manager_id, dept_id, first_name, last_name, title, salary)	VALUES	(6565,9856,01,'GHI','JKl','Security',19200)
 
select * from PRODUCT
select * from Department
select * from Employee

/* 11 */
EXEC sp_rename 'Dept', 'Department'
ALTER TABLE Department
ADD DEPARTMENT_SERVING_YEARS VARCHAR(20)

/* 12 */
Update Employee
set first_name = 'Ahmad'
where first_name = 'Ahmed'



