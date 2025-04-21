# This will hold all the information for the bank 

class Bank:
    """
     Class to represent a bank
     """
    def __init__(self):
        """
         Constructor to initialize the bank
         """
        self.account_number = 0
        self.pin = 0
        self.balance = 0
        self.name = ""
        self.email = ""
        self.phone = ""
        self.zip = ""
        self.country = ""
        self.bank_name = ""


accounts = [ 
    {
        "account_number": 123456,
        "pin": 1234,
        "balance": 1000,
        "name": "John",
        "surname": "Doe",
        "phone": "1234567890",
        "zip": "12345",
        "email": ""
    },
    {
        "account_number": 234567,
        "pin": 2345,
        "balance": 2000,
        "name": "Jane",
        "surname": "Doe",
        "phone": "0987654321",
        "zip": "54321",
        "email": ""
    }

]
