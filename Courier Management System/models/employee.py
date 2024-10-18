# models/employee.py

class Employee:
    def __init__(self, employeeID=None, employeeName=None, email=None,
                 contactNumber=None, role=None, salary=0.0):
        self.employeeID = employeeID
        self.employeeName = employeeName
        self.email = email
        self.contactNumber = contactNumber
        self.role = role
        self.salary = salary

    def __str__(self):
        return (f"Employee(ID: {self.employeeID}, Name: {self.employeeName}, "
                f"Email: {self.email}, Role: {self.role}, Salary: {self.salary})")
