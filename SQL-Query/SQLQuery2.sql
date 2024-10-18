--CREATE TABLE Students (
--    student_id INT IDENTITY(101,1) PRIMARY KEY,
--    gender CHAR(1) CHECK (gender IN ('M', 'F')),
--    age INT CHECK (age BETWEEN 5 AND 100)
--);
--GO

--INSERT INTO Students (gender, age)
--VALUES 
--('M', 15),
--('F', 22),
--('M', 10),
--('F', 30),
--('M', 18);

--CREATE TABLE Subjects (
--    subject_id INT IDENTITY(201,1) PRIMARY KEY,
--    subject_name VARCHAR(100) NOT NULL
--);
--GO

--INSERT INTO Subjects (subject_name)
--VALUES 
--('Mathematics'),
--('Physics'),
--('Chemistry'),
--('Biology');
 


--CREATE TABLE Subjects (
--    subject_id INT IDENTITY(201,1) PRIMARY KEY,
--    subject_name VARCHAR(100) NOT NULL
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
--    enrollment_id INT IDENTITY(301,1) PRIMARY KEY,
--    student_id INT,
--    subject_id INT,
--    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE,
--    FOREIGN KEY (subject_id) REFERENCES Subjects(subject_id) ON DELETE CASCADE
--);
--GO

--INSERT INTO Enrollments (student_id, subject_id)
--VALUES 
--(101, 201),  
--(101, 202), 
--(102, 201), 
--(102, 203),  
--(103, 204);  
--GO


select * from Students;
