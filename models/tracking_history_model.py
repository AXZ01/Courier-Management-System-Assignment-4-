# models/tracking_history_model.py

class TrackingHistory:
    def __init__(self):
        self.history = []

    def add_update(self, location_update):
        self.history.append(location_update)

    def get_history(self):
        return self.history
