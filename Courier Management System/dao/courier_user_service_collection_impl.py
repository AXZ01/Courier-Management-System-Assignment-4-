from services.i_courier_user_service import ICourierUserService
from models.courier_company_collection import CourierCompanyCollection


class CourierUserServiceCollectionImpl(ICourierUserService):
    def __init__(self):

        self.companyObj = CourierCompanyCollection()

    def place_order(self, courier_obj: CourierOrder):
        try:

            company = self.companyObj.get_company(courier_obj.company_id)
            if company:
                company.place_order(courier_obj)
                print(f"[SUCCESS] Order placed with tracking number {
                      courier_obj.tracking_number}")
            else:
                print(f"[ERROR] Company with ID {
                      courier_obj.company_id} not found.")
        except Exception as e:
            print(f"[ERROR] Failed to place the order: {e}")

    def get_order_status(self, tracking_number: str):
        try:

            company = self.companyObj.get_company_by_tracking_number(
                tracking_number)
            if company:
                status = company.get_order_status(tracking_number)
                print(f"Order Status for {tracking_number}: {status}")
            else:
                print(f"[ERROR] No company found for the tracking number {
                      tracking_number}")
        except Exception as e:
            print(f"[ERROR] Failed to get order status: {e}")

    def cancel_order(self, tracking_number: str):
        try:

            company = self.companyObj.get_company_by_tracking_number(
                tracking_number)
            if company:
                company.cancel_order(tracking_number)
                print(f"[SUCCESS] Order with tracking number {
                      tracking_number} has been canceled.")
            else:
                print(f"[ERROR] No company found for the tracking number {
                      tracking_number}")
        except Exception as e:
            print(f"[ERROR] Failed to cancel the order: {e}")

    def get_assigned_order(self, courier_staff_id: int):
        try:

            orders = self.companyObj.get_assigned_orders(courier_staff_id)
            if orders:
                print(f"Assigned orders for courier staff ID {
                      courier_staff_id}:")
                for order in orders:
                    print(f"Tracking Number: {
                          order.tracking_number}, Status: {order.status}")
            else:
                print(f"[INFO] No orders assigned to staff ID {
                      courier_staff_id}")
        except Exception as e:
            print(f"[ERROR] Failed to retrieve assigned orders: {e}")

    def add_company(self, company):
        try:
            self.companyObj.add_company(company)
            print(f"[SUCCESS] Company {company.name} added successfully.")
        except Exception as e:
            print(f"[ERROR] Failed to add the company: {e}")

    def get_company(self, company_id: int):
        try:
            company = self.companyObj.get_company(company_id)
            if company:
                return company
            else:
                print(f"[INFO] No company found with ID {company_id}")
        except Exception as e:
            print(f"[ERROR] Failed to retrieve the company: {e}")
        return None

    def remove_company(self, company_id: int):
        try:
            self.companyObj.remove_company(company_id)
            print(f"[SUCCESS] Company with ID {
                  company_id} removed successfully.")
        except Exception as e:
            print(f"[ERROR] Failed to remove the company: {e}")
