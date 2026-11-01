create database analytics;
use analytics;

CREATE TABLE department (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100)
);

CREATE TABLE employee (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  department_id INT,
  hire_date DATE,
  exit_date DATE NULL,
  FOREIGN KEY (department_id) REFERENCES department(id)
);

CREATE TABLE performance (
  id INT AUTO_INCREMENT PRIMARY KEY,
  employee_id INT,
  rating INT,  -- 1 to 5
  review_date DATE,
  FOREIGN KEY (employee_id) REFERENCES employee(id)
);

INSERT INTO department (name) VALUES
('Human Resources'),
('Finance'),
('Engineering'),
('Sales'),
('Marketing');

INSERT INTO employee (name, department_id, hire_date, exit_date) VALUES
('Alice Johnson', 1, '2021-04-10', NULL),
('Bob Smith', 1, '2020-01-15', '2023-09-20'),
('Charlie Brown', 2, '2022-03-01', NULL),
('David Thompson', 2, '2019-07-25', '2024-01-10'),
('Evelyn Carter', 3, '2020-11-11', NULL),
('Frank Miller', 3, '2018-05-03', NULL),
('Grace Lee', 3, '2021-02-18', '2023-12-01'),
('Hannah Williams', 4, '2024-05-19', NULL),
('Ian Clark', 4, '2022-09-10', NULL),
('Julia Davis', 5, '2020-03-22', NULL);


INSERT INTO performance (employee_id, rating, review_date) VALUES
(1, 4, '2024-12-31'),
(2, 3, '2023-08-10'),
(3, 5, '2025-01-15'),
(4, 2, '2024-02-28'),
(5, 4, '2025-03-01'),
(6, 5, '2025-08-20'),
(7, 3, '2023-11-30'),
(8, 4, '2025-09-15'),
(9, 2, '2024-05-22'),
(10, 5, '2025-10-01');


#-- run in MySQL client
CREATE DATABASE analytics CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;




DROP TABLE IF EXISTS performance;
DROP TABLE IF EXISTS employee;
DROP TABLE IF EXISTS department;


SELECT app, name, applied 
FROM django_migrations 
WHERE app = 'analytics';
