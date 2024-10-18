--CREATE TABLE CourierCompany (
--    CompanyID INT PRIMARY KEY IDENTITY(1,1),
--    CompanyName VARCHAR(100),
--    ContactNumber VARCHAR(15),
--    Email VARCHAR(100),
--    Address VARCHAR(255)
--);

--ALTER TABLE Courier
--ADD CompanyID INT,
--FOREIGN KEY (CompanyID) REFERENCES CourierCompany(CompanyID);

--ALTER TABLE Employee
--ADD CompanyID INT,
--FOREIGN KEY (CompanyID) REFERENCES CourierCompany(CompanyID);

--ALTER TABLE Locations
--ADD CompanyID INT,
--FOREIGN KEY (CompanyID) REFERENCES CourierCompany(CompanyID);

--INSERT INTO CourierCompany (CompanyName, ContactNumber, Email, Address) 
--VALUES 
--('Fast Delivery Co.', '1234567890', 'info@fastdelivery.com', '123 Delivery St., New York, NY'),
--('Quick Ship Logistics', '2345678901', 'support@quickship.com', '456 Shipping Blvd., Los Angeles, CA'),
--('Speedy Couriers', '3456789012', 'contact@speedycouriers.com', '789 Fast Lane, Chicago, IL'),
--('Express Freight Services', '4567890123', 'service@expressfreight.com', '321 Freight Ave., Houston, TX'),
--('Global Cargo Solutions', '5678901234', 'hello@globalcargo.com', '654 Cargo Rd., Miami, FL');

-- Update Employee to set CompanyID to 10
--UPDATE Employee
--SET CompanyID = 2
--WHERE EmployeeID = 1;

--UPDATE Employee
--SET CompanyID = 4
--WHERE EmployeeID = 2;

--UPDATE Employee
--SET CompanyID = 3
--WHERE EmployeeID = 3;

--UPDATE Employee
--SET CompanyID = 1
--WHERE EmployeeID = 4;

--UPDATE Employee
--SET CompanyID = 2
--WHERE EmployeeID = 5;

--UPDATE Employee
--SET CompanyID = 1
--WHERE EmployeeID = 6;

--UPDATE Employee
--SET CompanyID = 5
--WHERE EmployeeID = 7;

--UPDATE Employee
--SET CompanyID = 1
--WHERE EmployeeID = 8;

--UPDATE Employee
--SET CompanyID = 4
--WHERE EmployeeID = 9;

--UPDATE Employee
--SET CompanyID = 2
--WHERE EmployeeID = 10;

-- Update Courier to set CompanyID to 10
--UPDATE Courier
--SET CompanyID = 1
--WHERE CourierID = 1;

--UPDATE Courier
--SET CompanyID = 4
--WHERE CourierID = 2;

--UPDATE Courier
--SET CompanyID = 2
--WHERE CourierID = 3;

--UPDATE Courier
--SET CompanyID = 1
--WHERE CourierID = 4;

--UPDATE Courier
--SET CompanyID = 5
--WHERE CourierID = 5;

--UPDATE Courier
--SET CompanyID = 4
--WHERE CourierID = 6;

--UPDATE Courier
--SET CompanyID = 3
--WHERE CourierID = 7;

--UPDATE Courier
--SET CompanyID = 2
--WHERE CourierID = 8;

--UPDATE Courier
--SET CompanyID = 1
--WHERE CourierID = 9;

--UPDATE Courier
--SET CompanyID = 3
--WHERE CourierID = 10;

--select * from Employee;
--select * from Courier;
--select * from Users;
--select * from CourierCompany;

--SELECT EmployeeID, COUNT(*) AS TotalPackages
--FROM Courier
--GROUP BY EmployeeID;

--SELECT EmployeeID, AVG(DATEDIFF(DAY, OrderDate, DeliveryDate)) AS AverageDeliveryTime
--FROM Courier
--WHERE DeliveryDate IS NOT NULL AND OrderDate IS NOT NULL
--GROUP BY EmployeeID;

--SELECT u.UserID, u.UserName, c.CourierID, c.Status
--FROM Users u
--LEFT JOIN Courier c ON u.UserID = c.UserID;

--SELECT c.CourierID, c.SenderName, cs.ServiceID, cs.ServiceName
--FROM Courier c
--LEFT JOIN CourierServices cs ON c.ServiceID = cs.ServiceID;

--ALTER TABLE Courier
--ADD ServiceID INT;

--ALTER TABLE Courier
--ADD CONSTRAINT FK_Courier_Service
--FOREIGN KEY (ServiceID) REFERENCES CourierServices(ServiceID);

--UPDATE Courier
--SET ServiceID = CASE 
--                    WHEN CourierID = 1 THEN 1
--                    WHEN CourierID = 2 THEN 2
--                    WHEN CourierID = 3 THEN 1
--                    WHEN CourierID = 4 THEN 3
--                    WHEN CourierID = 5 THEN 2
--                    WHEN CourierID = 6 THEN 1
--                    WHEN CourierID = 7 THEN 3
--                    WHEN CourierID = 8 THEN 2
--                    WHEN CourierID = 9 THEN 1
--                    WHEN CourierID = 10 THEN 3
--                END
--WHERE CourierID BETWEEN 1 AND 10;

--SELECT c.CourierID, c.SenderName, cs.ServiceID, cs.ServiceName
--FROM Courier c
--LEFT JOIN CourierServices cs ON c.ServiceID = cs.ServiceID;  














