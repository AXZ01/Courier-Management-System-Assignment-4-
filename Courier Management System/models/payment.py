# models/payment.py

class Payment:
    def __init__(self, payment_id=None, courier_id=None, amount=None, payment_date=None):
        self.__payment_id = payment_id
        self.__courier_id = courier_id
        self.__amount = amount
        self.__payment_date = payment_date

    # Getters
    def get_payment_id(self):
        return self.__payment_id

    def get_courier_id(self):
        return self.__courier_id

    def get_amount(self):
        return self.__amount

    def get_payment_date(self):
        return self.__payment_date

    # Setters
    def set_courier_id(self, courier_id):
        self.__courier_id = courier_id

    def set_amount(self, amount):
        self.__amount = amount

    def set_payment_date(self, payment_date):
        self.__payment_date = payment_date

    def __str__(self):
        return f"Payment({self.__payment_id}, {self.__courier_id}, {self.__amount}, {self.__payment_date})"
