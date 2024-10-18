--CREATE TABLE Payment (
--    PaymentID INT PRIMARY KEY,
--    CourierID INT,
--    LocationID INT,
--    Amount DECIMAL(10, 2) NOT NULL,
--    PaymentDate DATE NOT NULL,
--    FOREIGN KEY (CourierID) REFERENCES Courier(CourierID),
--    FOREIGN KEY (LocationID) REFERENCES Locations(LocationID)
--);


--INSERT INTO Locations (LocationID, LocationName, Address) VALUES
--(1, 'Central Warehouse', '123 Main Street'),
--(2, 'Branch Office', '456 Secondary Street'),
--(3, 'Downtown Facility', '789 Downtown Road'),
--(4, 'Airport Hub', '555 Aviation Avenue'),
--(5, 'Westside Center', '888 Westside Drive');

--INSERT INTO Payment (PaymentID, CourierID, LocationID, Amount, PaymentDate) VALUES
--(1, 1, 1, 10.00, '2024-09-29'),
--(2, 2, 2, 20.00, '2024-09-30'),
--(3, 3, 3, 30.00, '2024-09-25'),
--(4, 4, 4, 50.00, '2024-10-01'),
--(5, 5, 5, 100.00, '2024-09-29');



--select * from Users;
--select * from Courier;
--select * from CourierServices;
--select * from Employee;
--select * from Locations;
--select * from Payment;


--INSERT INTO Users (UserID, Name, Email, Password, ContactNumber, Address) VALUES
--(6, 'Alice Johnson', 'alice@example.com', 'password222', '1231231234', '234 Elm Street'),
--(7, 'Bob Brown', 'bob@example.com', 'password333', '3213214321', '567 Oak Avenue'),
--(8, 'Charlie Black', 'charlie@example.com', 'password444', '4566544567', '678 Pine Road'),
--(9, 'Diana Prince', 'diana@example.com', 'password555', '6547893210', '789 Maple Drive'),
--(10, 'Ethan Hunt', 'ethan@example.com', 'password666', '7890123456', '456 Cedar Lane');

--INSERT INTO Courier (CourierID, SenderName, SenderAddress, ReceiverName, ReceiverAddress, Weight, Status, TrackingNumber, DeliveryDate, UserID) VALUES
--(6, 'Alice Johnson', '234 Elm Street', 'Greg Green', '987 Birch Boulevard', 1.5, 'Delivered', 'TRACK777', '2024-10-01', 6),
--(7, 'Alice Johnson', '234 Elm Street', 'Hannah White', '222 Ash Avenue', 2.0, 'In Transit', 'TRACK888', '2024-10-02', 6),
--(8, 'Alice Johnson', '234 Elm Street', 'Isaac Newton', '456 Willow Way', 3.0, 'In Transit', 'TRACK999', '2024-10-03', 6),
--(9, 'Bob Brown', '567 Oak Avenue', 'Kevin Smith', '999 Cherry Lane', 2.5, 'Delivered', 'TRACK101', '2024-09-30', 7),
--(10, 'Diana Prince', '789 Maple Drive', 'Lana Lang', '654 Spruce Street', 4.0, 'Delivered', 'TRACK202', '2024-09-29', 9);

--INSERT INTO CourierServices (ServiceID, ServiceName, Cost) VALUES
--(6, 'Budget Delivery', 5.00),
--(7, 'Priority Delivery', 15.00),
--(8, 'Heavy Load Delivery', 40.00),
--(9, 'Weekend Delivery', 60.00),
--(10, 'Same Hour Delivery', 80.00);


--INSERT INTO Employee (EmployeeID, Name, Email, ContactNumber, Role, Salary) VALUES
--(6, 'Tina Fey', 'tina@example.com', '1234567890', 'Delivery Manager', 70000.00),
--(7, 'Steve Carell', 'steve@example.com', '0987654321', 'Operations Supervisor', 60000.00),
--(8, 'Mindy Kaling', 'mindy@example.com', '1478523690', 'HR Manager', 55000.00),
--(9, 'Rashida Jones', 'rashida@example.com', '2589631470', 'Logistics Coordinator', 50000.00),
--(10, 'Ed Helms', 'ed@example.com', '3692581470', 'IT Support', 45000.00);

--INSERT INTO Locations (LocationID, LocationName, Address) VALUES
--(6, 'North Distribution Center', '321 North Road'),
--(7, 'South Distribution Center', '654 South Street'),
--(8, 'East Distribution Center', '987 East Lane'),
--(9, 'West Distribution Center', '123 West Drive'),
--(10, 'Central Distribution Hub', '456 Center Boulevard');

--INSERT INTO Payment (PaymentID, CourierID, LocationID, Amount, PaymentDate) VALUES
--(6, 6, 1, 15.00, '2024-10-01'),
--(7, 7, 2, 25.00, '2024-10-02'),
--(8, 8, 3, 35.00, '2024-10-03'),
--(9, 9, 4, 55.00, '2024-09-30'),
--(10, 10, 5, 45.00, '2024-09-29');


--select * from Users;

--SELECT * FROM Courier WHERE UserID =6 ;

--SELECT * FROM Courier;

--SELECT * FROM Courier WHERE CourierID= 2; 

--SELECT * FROM Courier WHERE CourierID = 9;

--SELECT * FROM Courier WHERE Status != 'Delivered';

--SELECT * FROM Courier WHERE DeliveryDate = CURRENT_DATE;

--SELECT * FROM Courier WHERE Status = 'In Transit';

--SELECT CourierID, COUNT(*) AS TotalPackages
--FROM Courier
--GROUP BY CourierID;

--SELECT * FROM Courier WHERE Weight BETWEEN 1.0 AND 3.0;

--SELECT * FROM Users WHERE Name LIKE 'John%';

SELECT * 
FROM Courier 
WHERE CourierID IN (SELECT CourierID FROM Payment WHERE Amount > 50);










