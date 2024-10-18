--CREATE table test (
--??testID int primary key,
--??name varchar(20)
--)

--CREATE table test1 (
--??testID int primary key,
--??name varchar(20) not null
--)

--insert into test (testID, name, age) values (5, 'Hiran', 19);
--insert into test values (4, 'Mahesh',16);
--go

--select * from test;

--Alter table test
--add age int not null default 16;

--insert into test (testID, name) values (6, 'Hiran');
--insert into test values (7, 'Hiran');
--insert into test values (7, 'Hiran', 18);

 

 
--alter table test
--add mobile varchar(10);



--update test
--set mobile = '9878964457' where testID = 1;

--update test
--set mobile = '9865745869' where testID= 2;

--update test
--set mobile = '9000124440' where testID = 3;

alter table test
add unique (mobile);

select * from test;