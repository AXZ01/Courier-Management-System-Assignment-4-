# services/order_confirmation_service.py

class OrderConfirmationService:
    def generate_confirmation_email(self, customer_name, order_number, delivery_address, expected_delivery_date):
        email_body = f"""
        Dear {customer_name},

        Thank you for your order!

        Order Number: {order_number}
        Delivery Address: {delivery_address}
        Expected Delivery Date: {expected_delivery_date}

        We appreciate your business and hope you enjoy your purchase!

        Best regards,
        XYZ Company
        """

        return email_body
