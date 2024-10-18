

# class DBConnUtil:
#     @staticmethod
#     def get_connection():
#         try:
#             conn = pyodbc.connect(
#                 "Driver={ODBC Driver 17 for SQL Server};"
#                 "Server=ABHILASH\\SQLEXPRESS02;"
#                 "Database=Assignment-4;"
#                 "UID=ABHILASH\\Abhi;"  # Keep this line if you want to specify a username
#                 "Trusted_Connection=yes;"  # This line will use Windows authentication
#             self.connection = self.connect()


import pyodbc


class DBConnUtil:
    def __init__(self):
        self.conn = None

    def connection(self):
        if not self.conn:
            self.conn = pyodbc.connect(
                "DRIVER={ODBC Driver 17 for SQL Server};"
                "SERVER=ABHILASH\\SQLEXPRESS02;"
                "DATABASE=Assignment-4;"
                "UID=ABHILASH\\Abhi;"
                "Trusted_Connection=yes;"
            )
        print("Database connection successful!")
        return self.conn
