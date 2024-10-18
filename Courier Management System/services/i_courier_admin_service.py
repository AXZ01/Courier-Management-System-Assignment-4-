# services/i_courier_admin_service.py

from abc import ABC, abstractmethod
from models.employee import Employee


class ICourierAdminService(ABC):

    @abstractmethod
    def add_courier_staff(self, obj: Employee) -> int:
        """Add a new courier staff member to the system.

        Args:
            obj (Employee): The employee object to be added.

        Returns:
            int: The ID of the newly added courier staff member.
        """
        pass
