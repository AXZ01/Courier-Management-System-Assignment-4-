from dao.courier_service_db import CourierServiceDb
# Assuming these exceptions exist
from exceptions import OrderNotFoundException, InvalidOrderStatusException, DatabaseConnectionException


def test_courier_service_db():
    service = CourierServiceDb()

    while True:
        print("\n====== Courier Management System ======")
        print("1. Insert Courier Order")
        print("2. Update Courier Order (by Tracking Number)")
        print("3. Retrieve Courier Details (by Tracking Number)")
        print("4. Retrieve Delivery History (by Tracking Number)")
        print("5. Generate Report")
        print("0. Exit")
        print("======================================")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("\n[ERROR] Invalid input. Please enter a valid number.")
            continue

        if choice == 0:
            print("\n[INFO] Exiting... Goodbye!")
            break

        elif choice == 1:
            # Insert Courier Order
            order_details = {}
            try:
                print("\n---- Insert Courier Order ----")
                order_details['courierID'] = int(input("Enter Courier ID: "))
                order_details['senderName'] = input("Enter Sender Name: ")
                order_details['senderAddress'] = input(
                    "Enter Sender Address: ")
                order_details['receiverName'] = input("Enter Receiver Name: ")
                order_details['receiverAddress'] = input(
                    "Enter Receiver Address: ")
                order_details['weight'] = float(
                    input("Enter Weight (e.g., 5.50): "))
                order_details['status'] = input("Enter Order Status: ")
                order_details['trackingNumber'] = input(
                    "Enter Tracking Number: ")
                order_details['deliveryDate'] = input(
                    "Enter Delivery Date (YYYY-MM-DD): ")
                order_details['userID'] = int(input("Enter User ID: "))
                order_details['employeeID'] = int(input("Enter Employee ID: "))
                order_details['locationID'] = int(input("Enter Location ID: "))
                order_details['orderDate'] = input(
                    "Enter Order Date (YYYY-MM-DD): ")
                order_details['companyID'] = int(input("Enter Company ID: "))

                service.insert_order(order_details)
                print("\n[SUCCESS] Courier order inserted successfully.")

            except ValueError as ve:
                print(f"\n[ERROR] Invalid input: {ve}")
            except DatabaseConnectionException as e:
                print(f"\n[ERROR] Database error: {e}")
            except Exception as e:
                print(f"\n[ERROR] Unexpected error: {e}")

        elif choice == 2:
            # Update Courier Order using Tracking Number
            print("\n---- Update Courier Order ----")
            try:
                tracking_number = input("Enter Tracking Number to update: ")
                new_status = input("Enter new Order Status: ")
                service.update_order(tracking_number, new_status)
                print(f"\n[SUCCESS] Order with Tracking Number {
                      tracking_number} updated successfully.")
            except OrderNotFoundException as e:
                print(f"\n[ERROR] {e}")
            except InvalidOrderStatusException as e:
                print(f"\n[ERROR] {e}")
            except Exception as e:
                print(f"\n[ERROR] Unexpected error: {e}")

        elif choice == 3:
            # Retrieve Courier Details using Tracking Number
            print("\n---- Retrieve Courier Details ----")
            try:
                tracking_number = input("Enter Tracking Number: ")
                details = service.retrieve_courier_details(tracking_number)
                if details:
                    print("\nCourier Details:")
                    print(f"Tracking Number: {details[8]}")
                    print(f"Sender Name: {details[1]}")
                    print(f"Receiver Name: {details[3]}")
                    print(f"Status: {details[6]}")
                    print(f"Delivery Date: {details[7]}")
                else:
                    print(f"\n[INFO] No details found for Tracking Number: {
                          tracking_number}")
            except OrderNotFoundException as e:
                print(f"\n[ERROR] {e}")
            except Exception as e:
                print(f"\n[ERROR] Unexpected error: {e}")

        elif choice == 4:
            # Retrieve Delivery History using Tracking Number
            print("\n---- Retrieve Delivery History ----")
            try:
                tracking_number = input("Enter Tracking Number: ")
                history = service.retrieve_delivery_history(tracking_number)
                if history:
                    print("\nDelivery History:")
                    for entry in history:
                        print(f"Courier ID: {entry[0]}, Status: {
                              entry[6]}, Delivery Date: {entry[7]}")
                else:
                    print(f"\n[INFO] No history found for Tracking Number: {
                          tracking_number}")
            except OrderNotFoundException as e:
                print(f"\n[ERROR] {e}")
            except Exception as e:
                print(f"\n[ERROR] Unexpected error: {e}")

        elif choice == 5:
            # Generate Report
            print("\n---- Generate Report ----")
            try:
                report = service.generate_report()
                if report:
                    print("\nCourier Report:")
                    for row in report:
                        print(f"Courier ID: {row[0]}, Sender: {row[1]}, Receiver: {
                              row[3]}, Status: {row[6]}, Delivery Date: {row[7]}")
                else:
                    print("\n[INFO] No report available.")
            except Exception as e:
                print(
                    f"\n[ERROR] Unexpected error while generating report: {e}")

        else:
            print("\n[ERROR] Invalid choice. Please select a valid option.")


# Uncomment the line below to run the test
test_courier_service_db()
