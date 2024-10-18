from models.employee_model import Employee
from models.user_model import User


class AuthService:
    def __init__(self, db_conn):
        self.db_conn = db_conn

    def authenticate_employee(self, employee_id, password):
        try:
            cursor = self.db_conn.cursor()
            cursor.execute("SELECT EmployeeID, Name, Password FROM Employee WHERE EmployeeID = ? AND Password = ?",
                           (employee_id, password))
            row = cursor.fetchone()

            if row:
                return f"Employee {row[1]} logged in successfully."
            else:
                return "Employee login failed. Please check your credentials."

        except Exception as e:
            return f"An error occurred during employee authentication: {str(e)}"

    def authenticate_user(self, username, password):
        try:
            cursor = self.db_conn.cursor()
            cursor.execute("SELECT UserID, Username, Password FROM Users WHERE Username = ? AND Password = ?",
                           (username, password))
            row = cursor.fetchone()

            if row:
                return f"User {row[1]} logged in successfully."
            else:
                return "User login failed. Please check your credentials."

        except Exception as e:
            return f"An error occurred during user authentication: {str(e)}"
