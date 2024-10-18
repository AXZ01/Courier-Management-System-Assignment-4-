--ALTER TABLE Courier 
--ADD OrderDate DATE;

--UPDATE Courier
--SET OrderDate = '2024-09-10' 
--WHERE CourierID = 1;

--UPDATE Courier
--SET OrderDate = '2024-09-15' 
--WHERE CourierID = 2;

--UPDATE Courier
--SET OrderDate = '2024-09-07' 
--WHERE CourierID = 3;

--UPDATE Courier
--SET OrderDate = '2024-09-20' 
--WHERE CourierID = 4;

--UPDATE Courier
--SET OrderDate = '2024-09-17' 
--WHERE CourierID = 5;

--UPDATE Courier
--SET OrderDate = '2024-09-22' 
--WHERE CourierID = 6;

--UPDATE Courier
--SET OrderDate = '2024-09-25' 
--WHERE CourierID = 7;

--UPDATE Courier
--SET OrderDate = '2024-09-16' 
--WHERE CourierID = 8;

--UPDATE Courier
--SET OrderDate = '2024-09-21' 
--WHERE CourierID = 9;

--UPDATE Courier
--SET OrderDate = '2024-09-12' 
--WHERE CourierID = 10;


--SELECT TOP 1 CourierID, 
--       AVG(DATEDIFF(day, ShipmentDate, DeliveryDate)) AS AvgDeliveryTime
--FROM Courier
--GROUP BY CourierID
--ORDER BY AvgDeliveryTime DESC;

--SELECT LocationID, SUM(Amount) AS TotalPayments
--FROM Payment
--GROUP BY LocationID
--HAVING SUM(Amount) < 2000;  
 
-- SELECT LocationID, SUM(Amount) AS TotalPayments
--FROM Payment
--GROUP BY LocationID;

--SELECT CourierID, SUM(Amount) AS TotalPayments
--FROM Payment
--WHERE LocationID = 3
--GROUP BY CourierID
--HAVING SUM(Amount) > 1000;

--SELECT CourierID, SUM(Amount) AS TotalPayments
--FROM Payment
--WHERE PaymentDate > '2024-09-25'  
--GROUP BY CourierID
--HAVING SUM(Amount) > 1000;



--SELECT LocationID, SUM(Amount) AS TotalPayments
--FROM Payment
--WHERE PaymentDate < '2024-09-29'  
--GROUP BY LocationID
--HAVING SUM(Amount) > 5000;

--SELECT p.*, c.*
--FROM Payment p
--INNER JOIN Courier c ON p.CourierID = c.CourierID;

--SELECT p.*, l.*
--FROM Payment p
--INNER JOIN Locations l ON p.LocationID = l.LocationID;

--SELECT p.*, c.*, l.*
--FROM Payment p
--INNER JOIN Courier c ON p.CourierID = c.CourierID
--INNER JOIN Locations l ON p.LocationID = l.LocationID;

--SELECT p.*, c.*
--FROM Payment p
--LEFT OUTER JOIN Courier c ON p.CourierID = c.CourierID;

--SELECT c.CourierID, SUM(p.Amount) AS TotalPayments
--FROM Payment p
--INNER JOIN Courier c ON p.CourierID = c.CourierID
--GROUP BY c.CourierID;

--SELECT *
--FROM Payment
--WHERE PaymentDate = '2024-09-29'; 

--SELECT p.*, c.*
--FROM Payment p
--INNER JOIN Courier c ON p.CourierID = c.CourierID;

--SELECT p.*, l.*
--FROM Payment p
--INNER JOIN Locations l ON p.LocationID = l.LocationID;

--SELECT c.CourierID, SUM(p.Amount) AS TotalPayments
--FROM Payment p
--INNER JOIN Courier c ON p.CourierID = c.CourierID
--GROUP BY c.CourierID;

--SELECT *
--FROM Payment
--WHERE PaymentDate BETWEEN '2024-09-25' AND '2024-09-30';  


--SELECT e.EmployeeID, e.Name AS EmployeeName, p.PaymentID, p.Amount
--FROM Employee e
--FULL OUTER JOIN Payment p ON e.EmployeeID = p.CourierID;  

--SELECT u.UserID, u.Name AS UserName, cs.ServiceID, cs.ServiceName
--FROM Users u
--CROSS JOIN CourierServices cs;

--SELECT e.EmployeeID, e.Name AS EmployeeName, l.LocationID, l.LocationName
--FROM Employee e
--CROSS JOIN Locations l;

--SELECT c.CourierID, c.SenderName, u.Name AS SenderUserName
--FROM Courier c
--LEFT OUTER JOIN Users u ON c.SenderName = u.Name; 

--SELECT c.CourierID, c.ReceiverName, u.Name AS ReceiverUserName
--FROM Courier c
--LEFT OUTER JOIN Users u ON c.ReceiverName = u.Name;  

--SELECT c.CourierID, c.TrackingNumber, cs.ServiceID, cs.ServiceName
--FROM Courier c
--LEFT OUTER JOIN CourierServices cs ON c.CourierID = cs.ServiceID;  

--SELECT e.EmployeeID, e.Name AS EmployeeName, COUNT(c.CourierID) AS CourierCount
--FROM Employee e
--LEFT JOIN Courier c ON e.EmployeeID = c.CourierID  

--SELECT l.LocationID, l.LocationName, SUM(p.Amount) AS TotalPayments
--FROM Locations l
--LEFT JOIN Payment p ON l.LocationID = p.LocationID
--GROUP BY l.LocationID, l.LocationName;

--SELECT c.SenderName, c.CourierID
--FROM Courier c
--WHERE c.SenderName IN (
--    SELECT SenderName
--    FROM Courier
--    GROUP BY SenderName
--    HAVING COUNT(CourierID) > 1
--);

--SELECT e.Role, e.EmployeeID, e.Name AS EmployeeName
--FROM Employee e
--WHERE e.Role IN (
--    SELECT Role
--    FROM Employee
--    GROUP BY Role
--    HAVING COUNT(EmployeeID) > 1
--);

ALTER TABLE Courier
ALTER COLUMN SenderAddress NVARCHAR(MAX);  


SELECT p.PaymentID, p.Amount, c.SenderAddress
FROM Payment p
JOIN Courier c ON p.CourierID = c.CourierID
WHERE c.SenderAddress LIKE (
    SELECT TOP 1 SenderAddress
    FROM Courier
    GROUP BY SenderAddress
    HAVING COUNT(CourierID) > 1
);



