from models.Account import Account
import datetime

class Loan:
    def __init__(self, account: Account, loan_type: str):
        self.account = account
        self.interest_rate = None
        self.date = datetime.date.today()
        self.loan_type = loan_type
        self.balance = 0.0
        self.amount = 0.0
        
