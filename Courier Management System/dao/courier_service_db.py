# dao/courier_service_db.py

import pyodbc
from db.db_conn_util import DBConnUtil


class CourierServiceDb:
    def __init__(self):
        self.connection = DBConnUtil.get_connection()

    def insert_order(self, order_details):
        cursor = self.connection.cursor()
        cursor.execute("""
            INSERT INTO dbo.Courier (CourierID, SenderName, SenderAddress, ReceiverName, ReceiverAddress, Weight, Status, 
                                    TrackingNumber, DeliveryDate, UserID, EmployeeID, LocationID, OrderDate, CompanyID)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            order_details['courierID'], order_details['senderName'], order_details['senderAddress'],
            order_details['receiverName'], order_details['receiverAddress'], order_details['weight'],
            order_details['status'], order_details['trackingNumber'], order_details['deliveryDate'],
            order_details['userID'], order_details['employeeID'], order_details['locationID'],
            order_details['orderDate'], order_details['companyID']
        ))
        self.connection.commit()
        print("Order inserted successfully.")

    def update_order(self, tracking_number, new_status):
        cursor = self.connection.cursor()
        cursor.execute("""
            UPDATE Courier
            SET Status = ?
            WHERE TrackingNumber = ?
        """, (new_status, tracking_number))
        self.connection.commit()

    def retrieve_courier_details(self, tracking_number):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT * FROM Courier
            WHERE TrackingNumber = ?
        """, (tracking_number,))
        return cursor.fetchone()

    def retrieve_delivery_history(self, tracking_number):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT * FROM Courier
            WHERE TrackingNumber = ?
        """, (tracking_number,))
        return cursor.fetchall()

    def generate_report(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Courier")
        return cursor.fetchall()
