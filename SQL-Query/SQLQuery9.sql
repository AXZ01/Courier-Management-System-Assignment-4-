--ALTER TABLE Courier
--ALTER COLUMN SenderAddress NVARCHAR(MAX);  

--SELECT p.PaymentID, p.Amount, c.SenderAddress
--FROM Payment p
--JOIN Courier c ON p.CourierID = c.CourierID
--WHERE c.SenderAddress LIKE (
--    SELECT TOP 1 SenderAddress
--    FROM Courier
--    GROUP BY SenderAddress
--    HAVING COUNT(CourierID) > 1
--);

--SELECT c.SenderAddress, c.CourierID
--FROM Courier c
--WHERE c.SenderAddress IN (
--    SELECT SenderAddress
--    FROM Courier
--    GROUP BY SenderAddress
--    HAVING COUNT(CourierID) > 1
--);

--SELECT e.EmployeeID, e.Name AS EmployeeName, COUNT(c.CourierID) AS DeliveredCouriers
--FROM Employee e
--LEFT JOIN Courier c ON e.EmployeeID = c.CourierID
--GROUP BY e.EmployeeID, e.Name;

--SELECT c.CourierID, p.Amount, cs.Cost
--FROM Courier c
--JOIN Payment p ON c.CourierID = p.CourierID
--JOIN CourierServices cs ON c.CourierID = cs.ServiceID  
--WHERE p.Amount > cs.Cost;

--SELECT *
--FROM Courier
--WHERE Weight > (SELECT AVG(Weight) FROM Courier);

--SELECT Name
--FROM Employee
--WHERE Salary > (SELECT AVG(Salary) FROM Employee);


--SELECT SUM(Cost) AS TotalCost
--FROM CourierServices
--WHERE Cost < (SELECT MAX(Cost) FROM CourierServices);


--SELECT *
--FROM Courier c
--WHERE EXISTS (
--    SELECT 1
--    FROM Payment p
--    WHERE p.CourierID = c.CourierID
--);

--SELECT l.LocationID, l.LocationName
--FROM Locations l
--WHERE EXISTS (
--    SELECT 1
--    FROM Payment p
--    WHERE p.LocationID = l.LocationID
--    AND p.Amount = (SELECT MAX(Amount) FROM Payment)
--);

SELECT *
FROM Courier c1
WHERE Weight > ALL (
    SELECT c2.Weight
    FROM Courier c2
    WHERE c2.SenderName = 'Alice Johnson'
);
