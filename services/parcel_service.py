from models.parcel_model import Parcel


class ParcelService:
    def __init__(self, db_conn):
        self.db_conn = db_conn

    def categorize_parcel(self, courier_id):
        try:
            # Retrieve parcel weight from the database based on courier_id
            cursor = self.db_conn.cursor()
            cursor.execute(
                "SELECT Weight FROM Courier WHERE CourierID = ?", (courier_id,))
            row = cursor.fetchone()

            if row:
                weight = row[0]
                # Create Parcel instance
                parcel = Parcel(courier_id, weight)

                # Switch-case-like structure using dictionary
                category = self.get_weight_category(parcel.get_weight())
                return f"Courier ID {courier_id} has a {category} parcel."

            else:
                return f"No courier found with ID {courier_id}."

        except Exception as e:
            return f"An error occurred: {str(e)}"

    def get_weight_category(self, weight):
        # Simulating switch-case behavior
        if weight <= 1:
            return "Light"
        elif 2 < weight <= 4:
            return "Medium"
        else:
            return "Heavy"
