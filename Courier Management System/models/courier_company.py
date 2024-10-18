# models/courier_company.py

class CourierCompany:
    def __init__(self, companyID, companyName):
        self.companyID = companyID
        self.companyName = companyName

    def __str__(self):
        return f"CourierCompany(companyID={self.companyID}, companyName={self.companyName})"
