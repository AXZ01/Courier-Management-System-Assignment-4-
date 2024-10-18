### >>>>>>>Task-1<<<<<<<###

######## Question-01##############

# from models.order_model import Order
# from services.order_service import OrderService


# def main():
#     # Create the order service
#     order_service = OrderService()

#     # Add some orders (these are sample orders)
#     order1 = Order(order_id=1, status="Processing")
#     order2 = Order(order_id=2, status="Delivered")
#     order3 = Order(order_id=3, status="Cancelled")

#     # Add orders to the service
#     order_service.add_order(order1)
#     order_service.add_order(order2)
#     order_service.add_order(order3)

#     # Prompt the user for an order ID
#     try:
#         order_id = int(input("Enter the Order ID to check its status: "))
#         # Check the status of the entered order ID
#         result = order_service.check_order_status(order_id)
#         print(result)
#     except ValueError:
#         print("Invalid input. Please enter a valid numeric Order ID.")


# if __name__ == "__main__":
#     main()


###### >Question-02<#####

# from utils.db_conn_util import DBConnUtil
# from services.parcel_service import ParcelService


# def main():
#     # Initialize database connection
#     db_conn = DBConnUtil().get_connection()

#     try:
#         # Create instance of ParcelService
#         parcel_service = ParcelService(db_conn)

#         # Ask user to input the courier ID
#         courier_id = int(
#             input("Enter the Courier ID to categorize the parcel: "))

#         # Call service to categorize parcel
#         result = parcel_service.categorize_parcel(courier_id)
#         print(result)

#     finally:
#         # Close the database connection
#         db_conn.close()


# if __name__ == "__main__":
#     main()


#### >Question-03<####

# from utils.db_conn_util import DBConnUtil
# from services.auth_service import AuthService


# def main():

#     db_conn = DBConnUtil().connection()

#     try:

#         auth_service = AuthService(db_conn)

#         user_type = input(
#             "Are you an Employee or User? (E/U): ").strip().upper()

#         if user_type == 'E':
#             employee_id = input("Enter your Employee ID: ")
#             password = input("Enter your password: ")
#             result = auth_service.authenticate_employee(employee_id, password)
#             print(result)

#         elif user_type == 'U':
#             username = input("Enter your Username: ")
#             password = input("Enter your password: ")
#             result = auth_service.authenticate_user(username, password)
#             print(result)

#         else:
#             print(
#                 "Invalid option. Please choose either 'E' for Employee or 'U' for User.")

#     finally:

#         db_conn.close()


# if __name__ == "__main__":
#     main()

#### >Question-04<####

# main.py

# from services.courier_assignment_service import CourierAssignmentService


# def main():
#     print("Courier Assignment System")
#     service = CourierAssignmentService()

#     while True:
#         print("1. Assign a courier to a shipment")
#         print("2. Exit")
#         choice = input("Enter your choice: ")

#         if choice == '1':
#             try:
#                 shipment_weight = float(
#                     input("Enter the shipment weight (in kg): "))
#                 shipment_proximity = float(
#                     input("Enter the maximum proximity (in km): "))

#                 assigned_couriers = service.assign_courier(
#                     shipment_weight, shipment_proximity)

#                 if assigned_couriers:
#                     print("Assigned Couriers:")
#                     for courier in assigned_couriers:
#                         print(courier)
#                 else:
#                     print("No couriers available for the given criteria.")
#             except ValueError:
#                 print("Invalid input. Please enter numeric values.")
#         elif choice == '2':
#             print("Exiting the program.")
#             break
#         else:
#             print("Invalid choice. Please select a valid option.")


# if __name__ == "__main__":
#     main()


# >>>>task-02<<<<<<<<<<
# >>>>>>>>question-05<<<<<<

# from utils.db_conn_util import DBConnUtil
# from services.order_service import CourierService


# def main():
#     db_conn = DBConnUtil().connection()
#     print("Database connection successful!")

#     while True:
#         print("Courier Management System")
#         print("1. Display couriers for a specific user")
#         print("2. Exit")
#         choice = int(input("Enter your choice: "))

#         if choice == 1:
#             #
#             user_id = int(input("Enter the User ID: "))
#             courier_service = CourierService(db_conn)
#             courier_service.display_couriers_for_user(user_id)
#         elif choice == 2:
#             break
#         else:
#             print("Invalid choice. Please try again.")


# if __name__ == "__main__":
#     main()


# >>>>Question-06<<<<<<

# from utils.db_conn_util import DBConnUtil
# from services.CourierService import CourierService


# def main():
#     # Database connection
#     db_conn = DBConnUtil().connection()

#     print("Database connection successful!")

#     courier_service = CourierService(db_conn)

#     while True:
#         print("Courier Tracking System")
#         print("1. Track a courier")
#         print("2. Exit")

#         choice = input("Enter your choice: ")

#         if choice == '1':
#             tracking_number = input("Enter the Tracking Number: ")
#             courier_service.track_courier(tracking_number)
#         elif choice == '2':
#             print("Exiting the program.")
#             break
#         else:
#             print("Invalid choice, please try again.")


# if __name__ == "__main__":
#     main()


# >>>>>>task-03<<<<<

# >>>Question-07<<<<<

# from utils.db_conn_util import DBConnUtil
# from services.CourierService import CourierService
# from services.tracking_history_service import TrackingHistoryService


# def main():
#     # Database connection
#     db_conn = DBConnUtil().connection()

#     print("Database connection successful!")

#     courier_service = CourierService(db_conn)
#     tracking_history_service = TrackingHistoryService()

#     while True:
#         print("Courier Tracking System")
#         print("1. Track a courier")
#         print("2. Add location update")
#         print("3. Display tracking history")
#         print("4. Exit")

#         choice = input("Enter your choice: ")

#         if choice == '1':
#             tracking_number = input("Enter the Tracking Number: ")
#             courier_info = courier_service.track_courier(tracking_number)

#             # Check delivery status
#             if courier_info:
#                 status = courier_info.get('Status')
#                 if status != 'Delivered':
#                     print(f"The current status of {
#                           tracking_number} is: {status}")
#                     # Option to update the delivery status
#                     update_status = input(
#                         "Do you want to update the delivery status to 'Delivered'? (yes/no): ")
#                     if update_status.lower() == 'yes':
#                         # Assuming there's a method in CourierService to update status
#                         courier_service.update_delivery_status(
#                             tracking_number, 'Delivered')
#                         print(f"Delivery status for {
#                               tracking_number} updated to 'Delivered'.")
#                     else:
#                         print("Continuing to track the courier.")
#             else:
#                 print("Courier not found.")

#         elif choice == '2':
#             tracking_number = input(
#                 "Enter the Tracking Number for the location update: ")
#             location_update = input("Enter the location update: ")
#             tracking_history_service.add_location_update(
#                 tracking_number, location_update)

#         elif choice == '3':
#             tracking_number = input(
#                 "Enter the Tracking Number to display tracking history: ")
#             tracking_history_service.display_tracking_history(tracking_number)

#         elif choice == '4':
#             print("Exiting the program.")
#             break

#         else:
#             print("Invalid choice, please try again.")


# if __name__ == "__main__":
#     main()

# >>>>>>question-08<<<<<<

# main.py

# from utils.db_conn_util import DBConnUtil
# from services.courier_service import CourierService


# def main():
#     # Database connection
#     db_conn = DBConnUtil().connection()

#     print("Database connection successful!")

#     courier_service = CourierService(db_conn)

#     # Add some couriers for demonstration (this would normally be from your database)
#     # Courier 1 at location (1, 2)
#     courier_service.add_courier(1, (1, 2), True)
#     # Courier 2 at location (3, 4)
#     courier_service.add_courier(2, (3, 4), False)
#     # Courier 3 at location (5, 1)
#     courier_service.add_courier(3, (5, 1), True)

#     while True:
#         print("Courier Assignment System")
#         print("1. Find nearest available courier")
#         print("2. Exit")

#         choice = input("Enter your choice: ")

#         if choice == '1':
#             order_location_input = input("Enter the order location (x,y): ")
#             # Convert input to tuple
#             order_location = tuple(map(int, order_location_input.split(',')))

#             nearest_courier = courier_service.find_nearest_available_courier(
#                 order_location)

#             if nearest_courier:
#                 print(f"The nearest available courier is: {nearest_courier}")
#             else:
#                 print("No available couriers found.")

#         elif choice == '2':
#             print("Exiting the program.")
#             break

#         else:
#             print("Invalid choice, please try again.")


# if __name__ == "__main__":
#     main()


# >>>>>>>>>question-09<<<<<<
# main.py

# from services.parcel_tracking_service import ParcelTrackingService
# from utils.db_conn_util import DBConnUtil


# def main():
#     db_conn = DBConnUtil().connection()  # Get the database connection
#     print("Database connection successful!")

#     print("Welcome to the Parcel Tracking System!")
#     tracking_service = ParcelTrackingService(db_conn)

#     while True:
#         tracking_number = input(
#             "Enter the parcel tracking number (or type 'exit' to quit): ")
#         if tracking_number.lower() == 'exit':
#             print("Exiting the Parcel Tracking System.")
#             break

#         # Get the status of the parcel
#         status = tracking_service.track_parcel(tracking_number)
#         print(f"Status for {tracking_number}: {status}")

#     db_conn.close()  # Close the database connection


# if __name__ == "__main__":
#     main()


# >>>>>question-10<<<<<<<

# from services.customer_validation_service import CustomerValidationService
# from utils.db_conn_util import DBConnUtil


# def main():
#     db_conn = DBConnUtil().connection()  # Get the database connection
#     print("Database connection successful!")


#     # Add a section for Customer Data Validation
#     validation_service = CustomerValidationService()

#     while True:
#         print("Customer Data Validation")
#         print("1. Validate Name")
#         print("2. Validate Address")
#         print("3. Validate Phone Number")
#         print("4. Exit")
#         choice = input("Enter your choice: ")

#         if choice == "1":
#             name = input("Enter the name: ")
#             is_valid, message = validation_service.validate_customer_info(
#                 name, "name")
#             print(message)

#         elif choice == "2":
#             address = input("Enter the address: ")
#             is_valid, message = validation_service.validate_customer_info(
#                 address, "address")
#             print(message)

#         elif choice == "3":
#             phone = input("Enter the phone number (###-###-####): ")
#             is_valid, message = validation_service.validate_customer_info(
#                 phone, "phone")
#             print(message)

#         elif choice == "4":
#             print("Exiting the Customer Data Validation System.")
#             break

#         else:
#             print("Invalid choice, please try again.")

#     db_conn.close()  # Close the database connection


# if __name__ == "__main__":
#     main()


# >>>>>Question-11<<<<<<<


# from services.address_formatting_service import AddressFormattingService


# def main():
#     print("Address Formatting System")
#     street = input("Enter street: ")
#     city = input("Enter city: ")
#     state = input("Enter state: ")
#     zip_code = input("Enter zip code: ")

#     address_service = AddressFormattingService()
#     formatted_address = address_service.format_address(
#         street, city, state, zip_code)

#     print("Formatted Address:", formatted_address)


# if __name__ == "__main__":
#     main()


# >>>>>Question-12<<<<<

# main.py
# from services.order_confirmation_service import OrderConfirmationService


# def main():
#     print("Order Confirmation Email Generator")

#     customer_name = input("Enter customer's name: ")
#     order_number = input("Enter order number: ")
#     delivery_address = input("Enter delivery address: ")
#     expected_delivery_date = input(
#         "Enter expected delivery date (YYYY-MM-DD): ")

#     confirmation_service = OrderConfirmationService()
#     email = confirmation_service.generate_confirmation_email(
#         customer_name,
#         order_number,
#         delivery_address,
#         expected_delivery_date
#     )

#     print("\nGenerated Order Confirmation Email:")
#     print(email)


# if __name__ == "__main__":
#     main()


# >>>>>>>>>>>Question-13<<<<<<<<<<<

# main.py
# from services.shipping_cost_service import ShippingCostService


# def main():
#     print("Shipping Cost Calculator")

#     source_address = input("Enter source address: ")
#     destination_address = input("Enter destination address: ")
#     weight = float(input("Enter weight of the parcel (in kg): "))

#     shipping_service = ShippingCostService()
#     shipping_cost = shipping_service.calculate_shipping_cost(
#         source_address, destination_address, weight)

#     print(f"\nCalculated Shipping Cost: ${shipping_cost:.2f}")


# if __name__ == "__main__":
#     main()


# >>>>>>Question-14<<<<<

# main.py
# from services.password_generator_service import PasswordGeneratorService


# def main():
#     print("Password Generator for Courier System Accounts")
#     length = int(input("Enter desired password length (minimum 8): "))

#     password_service = PasswordGeneratorService()

#     try:
#         password = password_service.generate_password(length)
#         print(f"\nGenerated Secure Password: {password}")
#     except ValueError as e:
#         print(e)


# if __name__ == "__main__":
#     main()


# >>>>>>>Question-15<<<<<

# main.py
# from services.address_similarity_service import AddressSimilarityService


# def main():
#     print("Address Similarity Finder")
#     addresses = [
#         "123 Elm St, Springfield, IL",
#         "123 Elm Street, Springfield, Illinois",
#         "456 Oak St, Springfield, IL",
#         "789 Pine St, Springfield, IL",
#         "123 E. Elm St., Springfield, IL",
#     ]

#     address_service = AddressSimilarityService(addresses)

#     target_address = input("Enter the address to find similar ones: ")
#     threshold = int(input("Enter similarity threshold (0-100): "))

#     similar_addresses = address_service.find_similar_addresses(
#         target_address, threshold)

#     if similar_addresses:
#         print("\nSimilar Addresses Found:")
#         for addr, score in similar_addresses:
#             print(f"{addr} (Similarity Score: {score})")
#     else:
#         print("No similar addresses found.")


# if __name__ == "__main__":
#     main()
