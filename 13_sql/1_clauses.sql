create database college1_db1;
use college1_db1;
create table student(
	students_id int primary key,
    name varchar(50) not null,
    email varchar(100) unique,
    age int check(age >= 18),
    course varchar(50) default 'BE',
    dept_id int    
);

create table departments(
	dept_id int primary key,
    dept_name varchar(50)
);

insert into student(students_id, name, email, age, course, dept_id) values
(1, 'Rahul', 'rahul@gamil.com', 20, 'BCA', 1),
(2, 'Priya', 'pr@gmail.com', 21, 'BE',2),
(3, 'Ram', 'rram@gmail.com', 22, 'BBA',1),
(4, 'Shri', 'shri@gmail.com', '23', 'BE', 1),
(5, 'Tejas', 'te@gmail.com', '20','B.com',3);

insert into departments (dept_id, dept_name) values
(1, 'Engineering'),
(2, 'Managment'),
(3, 'Commerce');

-- Foreign key
alter table student
add constraint fk_department
foreign key (dept_id)
references departments(dep_id);

describe student;

-- Where Clauses
select * from student where age > 21;
select * from student where age > 20 and course="BE";
select * from student where course in('BE','BCA');
select * from student where name like 'R%';

-- Orderby Clause
select * from student order by age asc;

-- distinct clause
select distinct courses from student;

-- aggregate / DAX function
select count(*) from student;
select avg(age) from student;
select max(age) from student;
select min(age) from student;


-- Group By Clause
select course, count(*) from student group by course;

-- having clause
select course, count(*) from student group by course having count(*) > 1;

-- sql query all cluase
select course,count(*)
from student
where age > 20 
group by course 
having count(*) > 1
order by course;










select * from student;
select * from departments;