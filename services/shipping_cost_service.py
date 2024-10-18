# services/shipping_cost_service.py

class ShippingCostService:
    def calculate_shipping_cost(self, source_address, destination_address, weight):

        distance = self.get_distance(source_address, destination_address)

        # Define cost per weight and cost per distance
        cost_per_weight = 5.0  # Cost per kg
        cost_per_distance = 2.0  # Cost per km

        # Calculate total shipping cost
        shipping_cost = (cost_per_weight * weight) + \
            (cost_per_distance * distance)
        return shipping_cost

    def get_distance(self, source_address, destination_address):

        return 10  # Assuming a fixed distance of 10 km for demonstration
