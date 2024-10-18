--ALTER TABLE Courier 
--ADD LocationID INT;

--ALTER TABLE Courier 
--ADD CONSTRAINT FK_Courier_Location
--FOREIGN KEY (LocationID) REFERENCES Location(LocationID);

--UPDATE Courier
--SET LocationID = 1
--WHERE CourierID  in (1,3);

--UPDATE Courier
--SET LocationID = 3
--WHERE CourierID in (2);

--UPDATE Courier
--SET LocationID = 2
--WHERE CourierID in (4,5);

--UPDATE Courier
--SET LocationID = 4
--WHERE CourierID in (6,8,10);

--UPDATE Courier
--SET LocationID = 6
--WHERE CourierID in (7);

--UPDATE Courier
--SET LocationID = 7
--WHERE CourierID in (9);

--SELECT LocationID, COUNT(CourierID) AS TotalCouriersDelivered
--FROM Courier
--GROUP BY LocationID;



UPDATE Courier
SET OrderDate = '2024-09-10' 
WHERE CourierID = 1;

UPDATE Courier
SET OrderDate = '2024-09-15' 
WHERE CourierID = 2;

UPDATE Courier
SET OrderDate = '2024-09-07' 
WHERE CourierID = 3;

UPDATE Courier
SET OrderDate = '2024-09-20' 
WHERE CourierID = 4;

UPDATE Courier
SET OrderDate = '2024-09-17' 
WHERE CourierID = 5;

UPDATE Courier
SET OrderDate = '2024-09-22' 
WHERE CourierID = 6;

UPDATE Courier
SET OrderDate = '2024-09-25' 
WHERE CourierID = 7;

UPDATE Courier
SET OrderDate = '2024-09-16' 
WHERE CourierID = 8;

UPDATE Courier
SET OrderDate = '2024-09-21' 
WHERE CourierID = 9;

UPDATE Courier
SET OrderDate = '2024-09-12' 
WHERE CourierID = 10;


SELECT * 
FROM Courier;
