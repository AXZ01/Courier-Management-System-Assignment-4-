# exceptions/exceptions.py

class TrackingNumberNotFoundException(Exception):
    """Exception raised when a tracking number is not found."""

    def __init__(self, message="Tracking number not found."):
        self.message = message
        super().__init__(self.message)


class InvalidEmployeeIdException(Exception):
    """Exception raised when an invalid employee ID is provided."""

    def __init__(self, message="Invalid employee ID provided."):
        self.message = message
        super().__init__(self.message)
