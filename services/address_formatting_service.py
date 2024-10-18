# services/address_formatting_service.py

import re


class AddressFormattingService:
    def format_address(self, street, city, state, zip_code):
        formatted_street = self.capitalize_words(street)
        formatted_city = self.capitalize_words(city)
        formatted_state = self.capitalize_words(state)
        formatted_zip_code = self.format_zip_code(zip_code)

        return f"{formatted_street}, {formatted_city}, {formatted_state}, {formatted_zip_code}"

    def capitalize_words(self, text):
        return ' '.join(word.capitalize() for word in text.split())

    def format_zip_code(self, zip_code):
        # Assuming zip code should be in the format "XXXXX" or "XXXXX-XXXX"
        if re.match(r'^\d{5}$', zip_code):
            return zip_code
        elif re.match(r'^\d{5}-\d{4}$', zip_code):
            return zip_code
        else:
            return "Invalid ZIP Code"
