# services/customer_validation_service.py

from models.customer_validation_model import CustomerValidation


class CustomerValidationService:
    def __init__(self):
        self.validator = CustomerValidation()

    def validate_customer_info(self, data, detail):
        return self.validator.validate(data, detail)
