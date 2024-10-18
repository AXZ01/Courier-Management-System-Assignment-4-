class Parcel:
    def __init__(self, courier_id, weight):
        self.courier_id = courier_id
        self.weight = weight

    def get_weight(self):
        return self.weight
