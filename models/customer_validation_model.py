# models/customer_validation_model.py

import re


class CustomerValidation:
    def validate(self, data, detail):
        if detail == "name":
            return self.validate_name(data)
        elif detail == "address":
            return self.validate_address(data)
        elif detail == "phone":
            return self.validate_phone(data)
        else:
            return False, "Invalid detail type."

    def validate_name(self, name):
        # Name should contain only letters and be capitalized
        if name.isalpha() and name == name.title():
            return True, "Name is valid."
        return False, "Invalid name. Names should only contain letters and be properly capitalized."

    def validate_address(self, address):
        # Address should not contain special characters
        if re.match("^[A-Za-z0-9\s,]*$", address):
            return True, "Address is valid."
        return False, "Invalid address. Addresses should not contain special characters."

    def validate_phone(self, phone):
        # Phone number format: ###-###-####
        if re.match(r"^\d{3}-\d{3}-\d{4}$", phone):
            return True, "Phone number is valid."
        return False, "Invalid phone number. Phone numbers should follow the format ###-###-####."
