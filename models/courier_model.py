# models/courier_model.py

# class Courier:
#     def __init__(self, courier_id, location, is_available):
#         self.courier_id = courier_id  # Courier ID
#         self.location = location        # Location of the courier
#         self.is_available = is_available  # Availability of the courier

#     def __repr__(self):
#         return f"Courier(ID: {self.courier_id}, Location: {self.location}, Available: {self.is_available})"


# >>>>>>task-01<<<<<
# >>>>Question-04<<<<<
# models/courier_model.py

class Courier:
    def __init__(self, courier_id, name, proximity, load_capacity):
        self.courier_id = courier_id
        self.name = name
        self.proximity = proximity  # in kilometers
        self.load_capacity = load_capacity  # in kg

    def __repr__(self):
        return f"Courier(ID: {self.courier_id}, Name: {self.name}, Proximity: {self.proximity}, Load Capacity: {self.load_capacity})"
