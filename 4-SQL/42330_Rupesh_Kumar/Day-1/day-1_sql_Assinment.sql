Task 1: Create Database - training _db

Solution:- 
>create database db_training;
>use db_training;

Task 2: Create students Table
Create a table named students with the following columns:
student_id*
student_name
age
course
city
enrollment_date
* student_id is primary key

Solution:-
> create table students(
    student_id int primary key,
    student_name varchar(50),
    age int,
    course varchar(50),
    city varchar(50),
    enrollment_date date
    );

> desc students;

Task 3: Insert Records
Insert at least 5 student records into the students table.

> insert into students values
   (1, 'Kumar', 20, 'SQL', 'Banglore', '2026-02-10'),
   (2, 'Kumar', 21, 'HTML', 'Patna', '2026-02-10'),
   (3, 'Kumar', 23, 'PYTHON', 'Banglore', '2026-02-10'),
   (4, 'Kumar', 19, 'SQL', 'KOLKATA', '2026-02-10'),
   (5, 'Kumar', 20, 'NODE', 'Banglore', '2026-02-10');

Data Retrieval:
>Display all columns from the students table.
> select * from students;

>Display only:
student_name
course

> select student_name, course from students;


>Display students who are enrolled in any one specific course of your choice.

>select * from students where course = 'SQL';


>Display students who belong to any one city of your choice.

>select * from students where city = 'Banglore';


>Display students whose age is greater than 20.

>select * from students where age > 20;


>List unique course names available in the table.
> select distinct course from students

>Display all students ordered by:
student_name in ascending order

>select * from students order by student_name asc;
 
Each participant must submit:
A single .sql file containing:
Database creation
Table creation
INSERT statements
All SELECT queries
 
Screenshot of:
Table structure
Output of SELECT * FROM student