# >>>>>>>>task-01<<<<<<<<

# from models.order_model import Order


# class OrderService:
#     def __init__(self):
#         self.orders = []  # Initialize with an empty list of orders

#     def add_order(self, order: Order):
#         """
#         Add an order to the list of orders.
#         """
#         self.orders.append(order)

#     def check_order_status(self, order_id):
#         for order in self.orders:
#             if order.get_order_id() == order_id:
#                 status = order.get_status()
#                 if status == "Delivered":
#                     return f"Order {order_id} has been delivered."
#                 elif status == "Processing":
#                     return f"Order {order_id} is still being processed."
#                 elif status == "Cancelled":
#                     return f"Order {order_id} was cancelled."
#                 else:
#                     return f"Order {order_id} has an unknown status: {status}"
#         return f"Order {order_id} not found."

# >>>>>>>task-02<<<<<<<
# >>>>Question-05<<<<<<<
# services/order_service.py

# import pyodbc


# class CourierService:
#     def __init__(self, db_conn):
#         self.db_conn = db_conn

#     def display_couriers_for_user(self, user_id):
#         try:
#             cursor = self.db_conn.cursor()
#             query = "SELECT CourierID, SenderName, ReceiverName, Weight, Status, TrackingNumber, OrderDate FROM Courier WHERE UserID = ?"
#             cursor.execute(query, (user_id,))
#             couriers = cursor.fetchall()

#             if couriers:
#                 print(f"Couriers for User ID {user_id}:")
#                 for courier in couriers:
#                     print(f"Courier ID: {courier.CourierID}, Sender: {courier.SenderName}, Receiver: {courier.ReceiverName}, Weight: {
#                           courier.Weight}, Status: {courier.Status}, Tracking Number: {courier.TrackingNumber}, Order Date: {courier.OrderDate}")
#             else:
#                 print("No couriers found for this user.")
#         except Exception as e:
#             print(f"Database error: {e}")
#         finally:
#             cursor.close()
