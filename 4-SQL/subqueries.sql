
CREATE DATABASE IF NOT EXISTS de_subquery_lab;

USE de_subquery_lab;
CREATE TABLE customers (
    customer_id   INT PRIMARY KEY AUTO_INCREMENT,
    name          VARCHAR(100) NOT NULL,
    city          VARCHAR(50)
);
CREATE TABLE orders (
    order_id      BIGINT PRIMARY KEY AUTO_INCREMENT,
    customer_id   INT NOT NULL,
    order_date    DATE NOT NULL,
    status        VARCHAR(20),
    total_amount  DECIMAL(10,2) NOT NULL,
    CONSTRAINT fk_orders_customer
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
INSERT INTO customers (name, city) VALUES
('Ankit',  'Bengaluru'),
('Meera',  'Hyderabad'),
('John',   'Pune'),
('Sara',   'Chennai'),
('Vikram', 'Bengaluru');

INSERT INTO orders (customer_id, order_date, status, total_amount) VALUES
(1, '2025-01-10', 'DELIVERED', 2500.00),
(1, '2025-02-05', 'DELIVERED', 1800.00),
(2, '2025-01-15', 'CANCELLED', 900.00),
(3, '2025-02-20', 'DELIVERED', 1200.00),
(3, '2025-03-11', 'DELIVERED', 3000.00),
(4, '2025-02-25', 'DELIVERED', 3500.00);
select * from customers;
select * from orders;
/* show all customers whose total spend is above the average order value */
/*scalar subquery(single value) */
SELECT
    c.customer_id,
    c.name,
    SUM(o.total_amount) AS total_spent
FROM customers AS c
JOIN orders AS o
    ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
HAVING SUM(o.total_amount) >
       (SELECT AVG(total_amount) FROM orders);

SELECT AVG(total_amount) FROM orders;
select distinct customer_id from orders where total_amount>2500;
select customer_id,name from customers where customer_id IN (select distinct customer_id from orders where total_amount>2500);

select o.order_id,o.customer_id,o.total_amount from orders o 
where o.total_amount >
(select avg(o2.total_amount) from orders o2 where o2.customer_id=o.customer_id);

select city,city_revenue from (select c.city, sum(o.total_amount) as city_revenue from customers c JOIN orders o ON c.customer_id=o.customer_id GROUP BY c.city) as city_stats where city_revenue>4000;

/* find customers who have at atleast 1 delivered order"

select c.customer_id,c.name from customers c where EXISTS(select 1 from orders o where o.customer_id=c.customer_id AND o.status='DELIVERED');

select c.customer_id,c.name from customers c where NOT EXISTS(select 1 from orders o where o.customer_id=c.customer_id);
