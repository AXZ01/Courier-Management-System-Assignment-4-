from services.i_courier_user_service import ICourierUserService
from models.courier_company import CourierCompany


class CourierUserServiceImpl(ICourierUserService):
    def __init__(self, company_obj: CourierCompany):
        self.company_obj = company_obj

    def place_order(self, courier_obj):
        try:

            self.company_obj.insert_courier_order(courier_obj)
            print("[SUCCESS] Order placed successfully.")
        except Exception as e:
            print(f"[ERROR] Failed to place order: {e}")

    def get_order_status(self, tracking_number: str):
        try:

            status = self.company_obj.get_courier_status_by_tracking_number(
                tracking_number)
            if status:
                print(f"[INFO] The status of order with Tracking Number {
                      tracking_number}: {status}")
            else:
                print(f"[INFO] No order found with Tracking Number: {
                      tracking_number}")
        except Exception as e:
            print(f"[ERROR] Failed to retrieve order status: {e}")

    def cancel_order(self, tracking_number: str):
        try:

            existing_order = self.company_obj.get_courier_by_tracking_number(
                tracking_number)
            if existing_order:

                self.company_obj.delete_courier_order(tracking_number)
                print(f"[SUCCESS] Order with Tracking Number {
                      tracking_number} has been canceled.")
            else:
                print(f"[INFO] No order found with Tracking Number: {
                      tracking_number}")
        except Exception as e:
            print(f"[ERROR] Failed to cancel order: {e}")

    def get_assigned_order(self, courier_staff_id: int):
        try:

            assigned_orders = self.company_obj.get_orders_assigned_to_staff(
                courier_staff_id)
            if assigned_orders:
                print(f"[INFO] Orders assigned to staff ID {
                      courier_staff_id}:")
                for order in assigned_orders:
                    print(f"Order ID: {order['orderID']}, Tracking Number: {
                          order['trackingNumber']}, Status: {order['status']}")
            else:
                print(f"[INFO] No orders found for staff ID: {
                      courier_staff_id}")
        except Exception as e:
            print(f"[ERROR] Failed to retrieve assigned orders: {e}")
