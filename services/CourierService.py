import pyodbc
import time


class CourierService:
    def __init__(self, db_conn):
        self.db_conn = db_conn

    def track_courier(self, tracking_number):
        cursor = self.db_conn.cursor()

        print(f"Tracking Courier with Tracking Number: {tracking_number}")

        while True:

            cursor.execute(
                "SELECT Status, DeliveryDate FROM Courier WHERE TrackingNumber = ?", (tracking_number,))
            result = cursor.fetchone()

            if result:
                status, delivery_date = result
                print(f"Current Status: {status}")

                # If the courier is delivered, exit the loop
                if status == "Delivered":
                    print("Courier has reached its destination!")
                    break
                elif status == "Cancelled":
                    print("The courier has been cancelled.")
                    break
            else:
                print("No courier found with the given Tracking Number.")
                break

            time.sleep(2)

        cursor.close()
