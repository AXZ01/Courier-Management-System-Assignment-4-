# services/courier_service.py

from models.courier_model import Courier


class CourierService:
    def __init__(self, db_conn):
        self.db_conn = db_conn
        self.couriers = []  # Array to hold couriers

    def add_courier(self, courier_id, location, is_available):
        # Method to add couriers to the array
        new_courier = Courier(courier_id, location, is_available)
        self.couriers.append(new_courier)

    def find_nearest_available_courier(self, order_location):
        nearest_courier = None
        min_distance = float('inf')

        for courier in self.couriers:
            if courier.is_available:
                distance = self.calculate_distance(
                    order_location, courier.location)
                if distance < min_distance:
                    min_distance = distance
                    nearest_courier = courier

        return nearest_courier

    def calculate_distance(self, loc1, loc2):
        # Dummy distance calculation (e.g., Manhattan distance for simplicity)
        return abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])
