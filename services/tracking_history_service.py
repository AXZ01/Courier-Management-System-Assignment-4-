# services/tracking_history_service.py

from models.tracking_history_model import TrackingHistory


class TrackingHistoryService:
    def __init__(self):
        # Dictionary to store tracking history by tracking number
        self.tracking_histories = {}

    def add_location_update(self, tracking_number, update):
        if tracking_number not in self.tracking_histories:
            self.tracking_histories[tracking_number] = TrackingHistory()
        self.tracking_histories[tracking_number].add_update(update)
        print(f"Location update added for {tracking_number}: {update}")

    def display_tracking_history(self, tracking_number):
        if tracking_number in self.tracking_histories:
            history = self.tracking_histories[tracking_number].get_history()
            if not history:
                print(f"No tracking history available for {tracking_number}.")
            else:
                print(f"Tracking History for {tracking_number}:")
                for update in history:
                    print(f"- {update}")
        else:
            print(f"No tracking history available for {tracking_number}.")
