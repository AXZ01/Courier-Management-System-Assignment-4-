# >>>>>task-01<<<<<

# class Order:
#     def __init__(self, order_id, status):
#         self.order_id = order_id
#         self.status = status

#     def get_order_id(self):
#         return self.order_id

#     def get_status(self):
#         return self.status

#     def set_status(self, status):
#         self.status = status

# >>>>>>>>>>>>>>>task-02<<<<<<<<<<<<<<<<<<

# models/order_model.py

class Order:
    def __init__(self, order_id, customer_id, order_date, status):
        self.order_id = order_id
        self.customer_id = customer_id
        self.order_date = order_date
        self.status = status

    def __str__(self):
        return f"Order ID: {self.order_id}, Customer ID: {self.customer_id}, Order Date: {self.order_date}, Status: {self.status}"
