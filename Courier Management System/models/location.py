# models/location.py

class Location:
    def __init__(self, location_id=None, location_name=None, address=None):
        self.__location_id = location_id
        self.__location_name = location_name
        self.__address = address

    # Getters
    def get_location_id(self):
        return self.__location_id

    def get_location_name(self):
        return self.__location_name

    def get_address(self):
        return self.__address

    # Setters
    def set_location_name(self, location_name):
        self.__location_name = location_name

    def set_address(self, address):
        self.__address = address

    def __str__(self):
        return f"Location({self.__location_id}, {self.__location_name}, {self.__address})"
