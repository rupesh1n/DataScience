show databases;
create database ds_sales;
create table customers(order_id int primary key, customer_id int, product varchar(50), price decimal(10,2), order_date date);
desc customers;
insert into customers values(1, 101, 'laptop', 30000.00, '2026-02-09'), (2, 101, 'camera', 20000.00, '2026-02-09');
select * from customers;

create table customers(customer_id int primary key, order_id int, product varchar(50), price decimal(10,2), order_date date);
select * from customers;
 insert into customers values(101, 1, 'laptop', 30000.00, '2026-02-09'), ( 102, 2, 'camera', 20000.00, '2026-02-09');
 select * from customers;
 insert into customers values(103, 1, 'laptop', 30000.00, '2026-02-19'), ( 104, 2, 'camera', 20000.00, '2026-02-19');
 select * from customers;