--CREATE TABLE Student (
--    sid INT PRIMARY KEY, 
--    name VARCHAR(50), 
--    age INT CHECK (age BETWEEN 16 AND 25), 
--    mobile VARCHAR(15) UNIQUE
--);

--CREATE TABLE Subjects (
--    sid INT PRIMARY KEY, 
--    subject1 VARCHAR(50), 
--    subject2 VARCHAR(50), 
--    subject3 VARCHAR(50),
--    FOREIGN KEY (sid) REFERENCES Student(sid)
--);

--CREATE TABLE Marks (
--    mark_id INT PRIMARY KEY,
--    sid INT, 
--    subject1_marks INT,
--    subject2_marks INT,
--    subject3_marks INT,
--    FOREIGN KEY (sid) REFERENCES Student(sid)
--);




--INSERT INTO Student (sid, name, age, mobile)
--VALUES 
--(1, 'John Doe', 20, '9876543210'),
--(2, 'Jane Smith', 22, '9876543211'),
--(3, 'Robert Brown', 19, '9876543212'),
--(4, 'Emily Davis', 21, '9876543213'),
--(5, 'Michael Wilson', 23, '9876543214');


--drop table Subjects;
--CREATE TABLE Subjects (
--    sid INT PRIMARY KEY, 
--    subject VARCHAR(50), 

--    FOREIGN KEY (sid) REFERENCES Student(sid)
--);

--INSERT INTO Subjects (sid, subject)
--VALUES 
--(1, 'Mathematics'),
--(2, 'Physics'),
--(3, 'Economics'),
--(4,  'Computer Science'),
--(5,  'Sociology');


--INSERT INTO Marks (mark_id, sid, subject1_marks)
--VALUES 
--(1, 1, 85, 90, 88),
--(2, 2, 78, 82, 89),
--(3, 3, 92, 87, 91),
--(4, 4, 88, 79, 93),
--(5, 5, 80, 85, 84);

--ALTER TABLE Marks
--DROP COLUMN subject2_marks;

--ALTER TABLE Marks
--DROP COLUMN subject3_marks;

--INSERT INTO Marks (mark_id, sid, subject_id, marks)
--VALUES 
--(1, 1, 1, 85),
--(2, 2, 2, 78),
--(3, 3, 3, 92),
--(4, 4, 4, 88),
--(5, 5, 5, 80);



select * from Student;
select * from Subjects;
select * from Marks;

--CREATE TABLE Marks (
--    mark_id INT PRIMARY KEY,
--    sid INT, 
--    marks INT,
--    FOREIGN KEY (sid) REFERENCES Student(sid)
--);


--INSERT INTO Marks (mark_id, sid, marks)
--VALUES 
--(1, 1, 85),
--(2, 2, 78),
--(3, 3, 92),
--(4, 4, 88),
--(5, 5, 80);
