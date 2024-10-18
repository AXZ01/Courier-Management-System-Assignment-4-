from models.courier_company import CourierCompany


class CourierCompanyCollection:
    def __init__(self):
        self.companies = []

    def add_company(self, company: CourierCompany):
        self.companies.append(company)

    def get_company(self, companyID: int):
        for company in self.companies:
            if company.companyID == companyID:
                return company
        return None

    def remove_company(self, companyID: int):
        self.companies = [
            company for company in self.companies if company.companyID != companyID]
