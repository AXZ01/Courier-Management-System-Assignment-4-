# services/parcel_tracking_service.py

from models.parcel_tracking_model import ParcelTracking


class ParcelTrackingService:
    def __init__(self, db_conn):
        self.tracking_model = ParcelTracking(db_conn)

    def track_parcel(self, tracking_number):
        # Get the status of the parcel from the model
        return self.tracking_model.get_status(tracking_number)
