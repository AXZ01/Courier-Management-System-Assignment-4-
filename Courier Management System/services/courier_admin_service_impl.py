from services.courier_user_service_impl import CourierUserServiceImpl
from services.i_courier_admin_service import ICourierAdminService
from models.employee import Employee


class CourierAdminServiceImpl(CourierUserServiceImpl, ICourierAdminService):
    def __init__(self, company_obj):
        super().__init__(company_obj)

    def add_courier_staff(self, employee: Employee):
        try:

            self.company_obj.insert_employee(employee)
            print(f"[SUCCESS] Courier staff {
                  employee.name} has been added successfully.")
        except Exception as e:
            print(f"[ERROR] Failed to add courier staff: {e}")

    def remove_courier_staff(self, employee_id: int):
        try:

            existing_employee = self.company_obj.get_employee_by_id(
                employee_id)
            if existing_employee:

                self.company_obj.delete_employee(employee_id)
                print(f"[SUCCESS] Courier staff with ID {
                      employee_id} has been removed successfully.")
            else:
                print(f"[INFO] No courier staff found with ID: {employee_id}")
        except Exception as e:
            print(f"[ERROR] Failed to remove courier staff: {e}")

    def assign_order_to_staff(self, tracking_number: str, employee_id: int):
        try:

            order = self.company_obj.get_courier_by_tracking_number(
                tracking_number)
            if order:

                employee = self.company_obj.get_employee_by_id(employee_id)
                if employee:

                    self.company_obj.assign_order_to_staff(
                        tracking_number, employee_id)
                    print(f"[SUCCESS] Order with Tracking Number {
                          tracking_number} has been assigned to Employee ID {employee_id}.")
                else:
                    print(f"[INFO] No courier staff found with ID: {
                          employee_id}")
            else:
                print(f"[INFO] No order found with Tracking Number: {
                      tracking_number}")
        except Exception as e:
            print(f"[ERROR] Failed to assign order: {e}")
