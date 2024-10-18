# services/courier_service.py

from models.courier import Courier
from models.employee import Employee
from services.i_courier_user_service import ICourierUserService
from services.i_courier_admin_service import ICourierAdminService
from exceptions.exceptions import TrackingNumberNotFoundException, InvalidEmployeeIdException


class CourierUserService(ICourierUserService):
    def __init__(self):
        self.orders = {}  # To store orders by tracking number
        self.tracking_number = 1000  # Initialize tracking number

    def place_order(self, courier_obj: Courier) -> str:
        self.tracking_number += 1  # Increment tracking number
        courier_obj.trackID = str(self.tracking_number)  # Assign tracking ID
        self.orders[courier_obj.trackID] = courier_obj
        return courier_obj.trackID

    def get_order_status(self, tracking_number: str) -> str:
        order = self.orders.get(tracking_number)
        if order:
            return order.status
        raise TrackingNumberNotFoundException(
            f"Tracking number {tracking_number} not found.")

    def cancel_order(self, tracking_number: str) -> bool:
        if tracking_number in self.orders:
            del self.orders[tracking_number]
            return True
        raise TrackingNumberNotFoundException(
            f"Tracking number {tracking_number} not found.")

    def get_assigned_order(self, courier_staff_id: int):
        # This is a placeholder; you'd implement logic to return assigned orders.
        return []


class CourierAdminService(ICourierAdminService):
    def __init__(self):
        self.staff = {}
        self.next_employee_id = 1

    def add_courier_staff(self, obj: Employee) -> int:
        obj.employeeID = self.next_employee_id
        self.staff[self.next_employee_id] = obj
        self.next_employee_id += 1
        return obj.employeeID

    def get_employee_by_id(self, employee_id: int) -> Employee:
        if employee_id not in self.staff:
            raise InvalidEmployeeIdException(
                f"Employee ID {employee_id} not found.")
        return self.staff[employee_id]
