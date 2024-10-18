# services/i_courier_user_service.py

from abc import ABC, abstractmethod
from models.courier import Courier


class ICourierUserService(ABC):
    tracking_number = 1000  # Static variable for unique tracking number

    @abstractmethod
    def place_order(self, courier_obj: Courier) -> str:
        """Place a new courier order.

        Args:
            courier_obj (Courier): Courier object created using values entered by users.

        Returns:
            str: The unique tracking number for the courier order.
        """
        pass

    @abstractmethod
    def get_order_status(self, tracking_number: str) -> str:
        """Get the status of a courier order.

        Args:
            tracking_number (str): The tracking number of the courier order.

        Returns:
            str: The status of the courier order (e.g., yetToTransit, In Transit, Delivered).
        """
        pass

    @abstractmethod
    def cancel_order(self, tracking_number: str) -> bool:
        """Cancel a courier order.

        Args:
            tracking_number (str): The tracking number of the courier order to be canceled.

        Returns:
            bool: True if the order was successfully canceled, False otherwise.
        """
        pass

    @abstractmethod
    def get_assigned_order(self, courier_staff_id: int):
        """Get a list of orders assigned to a specific courier staff member.

        Args:
            courier_staff_id (int): The ID of the courier staff member.

        Returns:
            list: A list of courier orders assigned to the staff member.
        """
        pass
