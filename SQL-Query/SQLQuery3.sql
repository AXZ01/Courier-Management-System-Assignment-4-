--CREATE TABLE Students (
--    student_id INT IDENTITY(101,1) PRIMARY KEY,
--    student_name VARCHAR(100) NOT NULL,
--    age INT CHECK (age BETWEEN 5 AND 100),
--    gender CHAR(1) CHECK (gender IN ('M', 'F'))
--);
--GO
--INSERT INTO Students (student_name, age, gender)
--VALUES 
--('John Doe', 15, 'M'),
--('Jane Smith', 22, 'F'),
--('Mike Johnson', 10, 'M'),
--('Emily Davis', 30, 'F'),
--('Chris Brown', 18, 'M');
--GO

--CREATE TABLE Subjects (
--    subject_id INT IDENTITY(201,1) PRIMARY KEY,
--    subject_name VARCHAR(100) NOT NULL CHECK (subject_name <> '')
--);
--GO
--INSERT INTO Subjects (subject_name)
--VALUES 
--('Mathematics'),
--('Physics'),
--('Chemistry'),
--('Biology');
--GO
--CREATE TABLE Enrollments (
--    enrollment_id INT IDENTITY(1,1) PRIMARY KEY,
--    student_id INT,
--    subject_id INT,
--    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE,
--    FOREIGN KEY (subject_id) REFERENCES Subjects(subject_id) ON DELETE CASCADE
--);
--GO
--INSERT INTO Enrollments (student_id, subject_id)
--VALUES 
--(101, 201),  
--(102, 202),  
--(103, 203),  
--(104, 204),  
--(101, 202);  
--GO

--UPDATE Students
--SET age = 23
--WHERE student_name = 'Jane Smith';
--GO

--CREATE TABLE Marks (
--    mark_id INT IDENTITY(1,1) PRIMARY KEY,
--    student_id INT,
--    subject_id INT,
--    marks INT CHECK (marks BETWEEN 0 AND 100),
--    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE,
--    FOREIGN KEY (subject_id) REFERENCES Subjects(subject_id) ON DELETE CASCADE
--);
--GO
--INSERT INTO Marks (student_id, subject_id, marks)
--VALUES 
--(101, 201, 85),  -- John Doe in Mathematics
--(101, 202, 90),  -- John Doe in Physics
--(102, 201, 78),  -- Jane Smith in Mathematics
--(102, 203, 88),  -- Jane Smith in Chemistry
--(103, 202, 95),  -- Mike Johnson in Physics
--(103, 204, 80);  -- Mike Johnson in Biology
--GO
--ALTER TABLE Students
--ADD email VARCHAR(255);
--GO

--UPDATE Students
--SET email = CASE student_id
--    WHEN 101 THEN 'john.doe@example.com'
--    WHEN 102 THEN 'jane.smith@example.com'
--    WHEN 103 THEN 'mike.johnson@example.com'
--    WHEN 104 THEN 'emily.davis@example.com'
--    END
--WHERE student_id IN (101, 102, 103, 104);
--GO



--	ALTER TABLE Marks
--DROP CONSTRAINT FK__Marks__subject_i__440B1D61;
--GO



--ALTER TABLE Marks
--ADD CONSTRAINT CHK_Marks_Range CHECK (marks BETWEEN 0 AND 100);
--GO


--SELECT 
--    s.student_name,
--    sub.subject_name
--FROM 
--    Students s
--LEFT JOIN 
--    Enrollments e ON s.student_id = e.student_id
--LEFT JOIN 
--    Subjects sub ON e.subject_id = sub.subject_id;
--GO


--SELECT 
--    s.student_id,
--    s.student_name,
--    sub.subject_name
--FROM 
--    Students s
--LEFT JOIN 
--    Enrollments e ON s.student_id = e.student_id
--LEFT JOIN 
--    Subjects sub ON e.subject_id = sub.subject_id;
--GO

--SELECT 
--    sub.subject_id,
--    sub.subject_name,
--    s.student_id
    
--FROM 
--    Subjects sub
--LEFT JOIN 
--    Enrollments e ON sub.subject_id = e.subject_id
--LEFT JOIN 
--    Students s ON e.student_id = s.student_id;
--GO

--SELECT 
--    s.student_id,
--    s.student_name,
--    sub.subject_id,
--    sub.subject_name
--FROM 
--    Students s
--FULL OUTER JOIN 
--    Enrollments e ON s.student_id = e.student_id
--FULL OUTER JOIN 
--    Subjects sub ON e.subject_id = sub.subject_id;
--GO


--create table Employees (
--    employee_id int identity(1,1) primary key,
--    employee_name varchar(100) not null,
--    manager_id int,
--    constraint FK_Employees_Employees foreign key (manager_id) references Employees(employee_id)
--);

--INSERT INTO Employees (employee_name, manager_id) VALUES 
--('Alice Johnson', NULL),     
--('Bob Smith', 1),           
--('Charlie Brown', 1),        
--('Diana Prince', 2),         
--('Edward Nygma', 3);         
--GO

--SELECT 
--    e.employee_id AS EmployeeID,
--    e.employee_name AS EmployeeName,
--    m.employee_name AS ManagerName
--FROM 
--    Employees e
--LEFT JOIN 
--    Employees m ON e.manager_id = m.employee_id;
--GO

--SELECT 
--    s.student_id,
--    s.student_name,
--    sub.subject_id,
--    sub.subject_name
--FROM 
--    Students s
--FULL OUTER JOIN 
--    Enrollments e ON s.student_id = e.student_id
--FULL OUTER JOIN 
--    Subjects sub ON e.subject_id = sub.subject_id;
--GO


--SELECT 
--    s.student_id,
--    s.student_name,
--    sub.subject_id,
--    sub.subject_name
--FROM 
--    Students s
--CROSS JOIN 
--    Subjects sub;
--GO


--SELECT 
--    s.student_id,
--    s.student_name,
--    SUM(m.marks) AS total_marks
--FROM 
--    Students s
--LEFT JOIN 
--    Marks m ON s.student_id = m.student_id
--GROUP BY 
--    s.student_id, s.student_name;
--GO
--select * from Enrollments;

--SELECT 
--    s.student_id,
--    s.student_name,
--    sub.subject_name
--FROM 
--    Students s
--LEFT JOIN 
--    Enrollments e ON s.student_id = e.student_id
--LEFT JOIN 
--    Subjects sub ON e.subject_id = sub.subject_id;
GO
