import datetime
from models.AccountHolder import AccountHolder


class Account:
    def __init__(self, email: AccountHolder):
        self.account_holder = email
        self.balance = 0.0
        self.email = None
        self.date_created = datetime.date.today()
        self.account_status = 'active'
