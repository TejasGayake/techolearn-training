create database Company_db17;
use Company_db17;

create table department(
	dept_id int primary key,
    dept_name varchar(50)
);

create table employee(
	emp_id int primary key,
    emp_name varchar(50),
    salary int,
    dept_id int,
    foreign key (dept_id) references department(dept_id)
);

insert into department value
(1,'HR'),
(2,'IT'),
(3,'Finance');

insert into employee value
(101,'swrp',40000,1),
(102,'sneha',60000,2),
(103,'surty',55000,2),
(104,'hrish',75000,3),
(105,'mndr',90000,2);

select * from employee;
select * from department;


-- SUBQUERY

-- 1 SINGLE ROW SUBQUERY
select emp_name ,salary from employee
where salary  = (select max(salary) from employee);

-- 2) Multilevel query
select emp_name,dept_id
from employee 
where dept_id 
in(select dept_id
   from department 
   where dept_name 
   in('IT','HR')
);

-- 3) Correlated subquery
select e1.emp_name,e1.salary from employee e1
where e1.salary > (select avg(e2.salary) from employee e2
where e1.dept_id = e2.dept_id );