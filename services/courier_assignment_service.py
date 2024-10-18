# services/courier_assignment_service.py

from models.courier_model import Courier


class CourierAssignmentService:
    def __init__(self):
        # Example courier data; this should be fetched from the database in real applications
        self.couriers = [
            Courier(1, "Courier A", 5, 10),  # 5 km proximity, 10 kg capacity
            Courier(2, "Courier B", 10, 15),  # 10 km proximity, 15 kg capacity
            Courier(3, "Courier C", 3, 8),    # 3 km proximity, 8 kg capacity
            Courier(4, "Courier D", 7, 12),   # 7 km proximity, 12 kg capacity
        ]

    def assign_courier(self, shipment_weight, shipment_proximity):
        # Criteria: Find couriers who can handle the shipment weight and are within proximity
        assigned_couriers = []

        for courier in self.couriers:
            if courier.load_capacity >= shipment_weight and courier.proximity <= shipment_proximity:
                assigned_couriers.append(courier)

        return assigned_couriers
