import random
import string


class PasswordGeneratorService:
    def generate_password(self, length=12):
        if length < 8:  # Ensure minimum length for security
            raise ValueError(
                "Password length should be at least 8 characters.")

        # Define character pools
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        digits = string.digits
        special = string.punctuation

        # Ensure the password contains at least one character from each category
        password = [
            random.choice(lower),
            random.choice(upper),
            random.choice(digits),
            random.choice(special)
        ]

        # Fill the rest of the password length with random choices
        all_characters = lower + upper + digits + special
        password += random.choices(all_characters, k=length - 4)

        # Shuffle the password to avoid predictable patterns
        random.shuffle(password)

        return ''.join(password)
