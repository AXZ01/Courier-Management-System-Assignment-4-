# models/parcel_tracking_model.py

import pyodbc


class ParcelTracking:
    def __init__(self, db_conn):
        self.db_conn = db_conn
        self.tracking_data = self.fetch_tracking_data()

    def fetch_tracking_data(self):
        tracking_data = []
        try:
            cursor = self.db_conn.cursor()
            query = "SELECT TrackingNumber, Status FROM Courier"
            cursor.execute(query)

            for row in cursor.fetchall():
                tracking_data.append([row.TrackingNumber, row.Status])

            cursor.close()
        except Exception as e:
            print(f"Database error: {e}")

        return tracking_data

    def get_status(self, tracking_number):
        # Search for the tracking number in the tracking_data array
        for parcel in self.tracking_data:
            if parcel[0] == tracking_number:
                return parcel[1]
        return "Tracking number not found"
