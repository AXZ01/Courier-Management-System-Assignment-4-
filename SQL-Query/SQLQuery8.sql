--ALTER TABLE Courier 
--ADD EmployeeID INT;

--ALTER TABLE Courier 
--ADD CONSTRAINT FK_Courier_Employee
--FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID);


--UPDATE Courier
--SET EmployeeID = 1
--WHERE CourierID IN (1, 2);

--UPDATE Courier
--SET EmployeeID = 2
--WHERE CourierID IN (3);

--UPDATE Courier
--SET EmployeeID = 5
--WHERE CourierID IN (4, 5);

--UPDATE Courier
--SET EmployeeID = 3
--WHERE CourierID IN (6,7);

--UPDATE Courier
--SET EmployeeID = 6
--WHERE CourierID IN (8, 9,10);


--SELECT EmployeeID, COUNT(CourierID) AS TotalCouriers
--FROM Courier
--GROUP BY EmployeeID;

--SELECT LocationID, SUM(Amount) AS TotalRevenue
--FROM Payment
--GROUP BY LocationID;


--ALTER TABLE Courier 
--ADD LocationID INT;

--ALTER TABLE Courier 
--ADD CONSTRAINT FK_Courier_Location
--FOREIGN KEY (LocationID) REFERENCES Locations(LocationID);

