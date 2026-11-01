CREATE DATABASE IF NOT EXISTS training_index_lab;
USE training_index_lab;

CREATE TABLE customers (
    customer_id   INT PRIMARY KEY AUTO_INCREMENT,
    name          VARCHAR(100) NOT NULL,
    email         VARCHAR(100) NOT NULL,
    city          VARCHAR(50),
    created_at    DATETIME NOT NULL
);

CREATE TABLE orders (
    order_id      BIGINT PRIMARY KEY AUTO_INCREMENT,
    customer_id   INT NOT NULL,
    order_date    DATETIME NOT NULL,
    status        VARCHAR(20),
    total_amount  DECIMAL(10,2),
    CONSTRAINT fk_orders_customer
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
INSERT INTO customers (name, email, city, created_at) VALUES
('Ankit',  'ankit@example.com',  'Bengaluru', NOW() - INTERVAL 30 DAY),
('Meera',  'meera@example.com',  'Hyderabad', NOW() - INTERVAL 25 DAY),
('John',   'john@example.com',   'Pune',      NOW() - INTERVAL 20 DAY),
('Sara',   'sara@example.com',   'Chennai',   NOW() - INTERVAL 10 DAY),
('Vikram', 'vikram@example.com', 'Bengaluru', NOW() - INTERVAL 5 DAY);

INSERT INTO orders (customer_id, order_date, status, total_amount) VALUES
(1, NOW() - INTERVAL 9 DAY,  'PLACED',   2500.00),
(1, NOW() - INTERVAL 2 DAY,  'SHIPPED',  1800.00),
(2, NOW() - INTERVAL 15 DAY, 'CANCELLED',900.00),
(3, NOW() - INTERVAL 7 DAY,  'PLACED',   1200.00),
(4, NOW() - INTERVAL 3 DAY,  'DELIVERED',3500.00);
select * from customers;

select * from orders;

select c.customer_id,c.name,c.city,o.order_id,o.order_date,o.total_amount from customers c JOIN
orders o ON c.customer_id=o.customer_id where c.city='Bengaluru' AND o.order_date >= now() - interval 10 day;

create index idx_customers_city on customers(city);

select c.customer_id,c.name,c.city,o.order_id,o.order_date,o.total_amount from customers c JOIN
orders o ON c.customer_id=o.customer_id where c.city='Bengaluru' AND o.order_date >= now() - interval 10 day;

show indexes from orders;
drop index idx_customers_city ON customers;

create index idx_orders_customers_date ON orders(customer_id,order_date);