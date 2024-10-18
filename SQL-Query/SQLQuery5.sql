--CREATE TABLE Users (
--    UserID INT PRIMARY KEY,
--    Name VARCHAR(255) NOT NULL,
--    Email VARCHAR(255) UNIQUE NOT NULL,
--    Password VARCHAR(255) NOT NULL,
--    ContactNumber VARCHAR(20),
--    Address TEXT
--);
--CREATE TABLE Courier (
--    CourierID INT PRIMARY KEY,
--    SenderName VARCHAR(255) NOT NULL,
--    SenderAddress TEXT NOT NULL,
--    ReceiverName VARCHAR(255) NOT NULL,
--    ReceiverAddress TEXT NOT NULL,
--    Weight DECIMAL(5, 2) NOT NULL,
--    Status VARCHAR(50) NOT NULL,
--    TrackingNumber VARCHAR(20) UNIQUE NOT NULL,
--    DeliveryDate DATE,
--    UserID INT,
--    FOREIGN KEY (UserID) REFERENCES Users(UserID)
--);
--CREATE TABLE CourierServices (
--    ServiceID INT PRIMARY KEY,
--    ServiceName VARCHAR(100) NOT NULL,
--    Cost DECIMAL(8, 2) NOT NULL
--);
--CREATE TABLE Employee (
--    EmployeeID INT PRIMARY KEY,
--    Name VARCHAR(255) NOT NULL,
--    Email VARCHAR(255) UNIQUE NOT NULL,
--    ContactNumber VARCHAR(20),
--    Role VARCHAR(50),
--    Salary DECIMAL(10, 2) NOT NULL
--);
--CREATE TABLE Location (
--    LocationID INT PRIMARY KEY,
--    LocationName VARCHAR(100) NOT NULL,
--    Address TEXT NOT NULL
--);
--CREATE TABLE Payment (
--    PaymentID INT PRIMARY KEY,
--    CourierID INT,
--    LocationID INT,
--    Amount DECIMAL(10, 2) NOT NULL,
--    PaymentDate DATE NOT NULL,
--    FOREIGN KEY (CourierID) REFERENCES Courier(CourierID),
--    FOREIGN KEY (LocationID) REFERENCES Location(LocationID)
--);



--INSERT INTO Users (UserID, Name, Email, Password, ContactNumber, Address) VALUES
--(1, 'John Doe', 'john@example.com', 'password123', '1234567890', '123 Elm Street'),
--(2, 'Jane Smith', 'jane@example.com', 'password456', '0987654321', '456 Oak Avenue'),
--(3, 'Robert Johnson', 'robert@example.com', 'password789', '1122334455', '789 Pine Street'),
--(4, 'Emily Clark', 'emily@example.com', 'password000', '5566778899', '321 Maple Avenue'),
--(5, 'Chris Evans', 'chris@example.com', 'password111', '6677889900', '654 Oak Lane');


--INSERT INTO Courier (CourierID, SenderName, SenderAddress, ReceiverName, ReceiverAddress, Weight, Status, TrackingNumber, DeliveryDate, UserID) VALUES
--(1, 'John Doe', '123 Elm Street', 'Alice Johnson', '789 Pine Road', 2.5, 'Delivered', 'TRACK123', '2024-09-28', 1),
--(2, 'Jane Smith', '456 Oak Avenue', 'Bob Brown', '101 Maple Drive', 3.0, 'In Transit', 'TRACK456', '2024-09-30', 2),
--(3, 'Robert Johnson', '789 Pine Street', 'Mike Tyson', '555 Birch Avenue', 1.8, 'Delivered', 'TRACK789', '2024-09-25', 3),
--(4, 'Emily Clark', '321 Maple Avenue', 'Sophia Loren', '333 Cedar Boulevard', 4.2, 'In Transit', 'TRACK321', '2024-10-01', 4),
--(5, 'Chris Evans', '654 Oak Lane', 'David Warner', '888 Walnut Street', 6.5, 'Delivered', 'TRACK654', '2024-09-29', 5);


--INSERT INTO CourierServices (ServiceID, ServiceName, Cost) VALUES
--(1, 'Standard Delivery', 10.00),
--(2, 'Express Delivery', 20.00),
--(3, 'Overnight Delivery', 30.00),
--(4, 'Same Day Delivery', 50.00),
--(5, 'International Delivery', 100.00);


--INSERT INTO Employee (EmployeeID, Name, Email, ContactNumber, Role, Salary) VALUES
--(1, 'Michael Scott', 'michael@example.com', '1234567890', 'Branch Manager', 60000.00),
--(2, 'Pam Beesly', 'pam@example.com', '0987654321', 'Receptionist', 35000.00),
--(3, 'Jim Halpert', 'jim@example.com', '1478523690', 'Salesman', 50000.00),
--(4, 'Dwight Schrute', 'dwight@example.com', '2589631470', 'Assistant Regional Manager', 55000.00),
--(5, 'Stanley Hudson', 'stanley@example.com', '3692581470', 'Salesman', 45000.00);


--INSERT INTO Location (LocationID, LocationName, Address) VALUES
--(1, 'Central Warehouse', '123 Main Street'),
--(2, 'Branch Office', '456 Secondary Street'),
--(3, 'Downtown Facility', '789 Downtown Road'),
--(4, 'Airport Hub', '555 Aviation Avenue'),
--(5, 'Westside Center', '888 Westside Drive');


INSERT INTO Payment (PaymentID, CourierID, LocationID, Amount, PaymentDate) VALUES
(1, 1, 1, 10.00, '2024-09-29'),
(2, 2, 2, 20.00, '2024-09-30'),
(3, 3, 3, 30.00, '2024-09-25'),
(4, 4, 4, 50.00, '2024-10-01'),
(5, 5, 5, 100.00, '2024-09-29');


