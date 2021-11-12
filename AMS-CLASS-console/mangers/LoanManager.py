from models.Loan import Loan
from models.Account import Account
from typing import List

class LoanManager:
    Loans: List[Loan] = []

    loan_types = {
        'household': 100000,
        'car': 500000,
        'school fee': 200000,
        'business': 1000000,
        'emergency': 50000
    }

    


    def create_loan(self, email: Account, loan_type: str, number_of_months: int):
        loan = Loan(account=email, loan_type=loan_type)
        if_any_loan_active = self.__check_if_no_active_loan(account_number=loan.account.account_number)
        if if_any_loan_active is True:
            print("Sorry you will have to pay up first")
        else:
            loan.amount = self.__get_loan_amount_by_loan_type(loan_type=loan_type)
            loan.status = 'active'
            loan.interest_rate = self.__get_loan_interest_rate(number_of_months == number_of_months)
            loan.balance = self.__get_loan_initial_balance(interest_rate=loan.interest_rate, amount=loan.amount)
            loan.loan_type = loan_type
            loan.id = self.__get_id()
            self.Loans.append(Loan)
            print("Loan has been granted your loan amount is", loan.amount, "You will pay up in the next", number_of_months )
            

    def list_loan(self):
        for loan in self.loans:
            self.__show(loan)

    def pay_back(self, email: str, amount: float):
        loan = self.__get_loan(email=email)
        if loan is not False:
            loan.balance -= amount
            if loan.balance == 0:
                loan.status = 'inactive'
                print("Loan sussefully paid")
                
            else:
                print('Pls you will have to pay up your remaining loan balance, pls pay up to acquire another loan and your loan balance is', loan.balance)
        else:
            print("No active loan found")
    def search(self, email: str):
        # search and returns the account holder if not None

        loan = self.__find(email)
        if loan is None:
            return False
        else:
            self.__show(loan)

    def __check_if_no_active_loan(self, email: str):
        for loan in self.loans:
            if loan.account.account_number == email:
                if loan.status == 'active':
                    return True
        return False

    def __get_loan_amount_by_loan_type(self, loan_type: str):
        for loan in self.loan_types:
            if loan == loan_type:
                return self.loan_types[loan]

    def __find(self, email: str): 
        for loan in self.loans:
            if loan.account.account_number == email:
                return loan
            else:
                return None


    def __get_loan_interest_rate(self, number_of_months: int):
        interest_rate = number_of_months / 100
        return interest_rate

    def __get_loan_initial_balance(self, interest_rate: int, amount:int):
        val = interest_rate * amount
        amount += val
        return val

    def __get_id(self):
        length = len(self.loans)
        if length == 0:
            length += 1
            return length
        else:
            for loan in self.loans:
                if loan.id == length:
                    length += 1
                    return length
                else:
                    continue

    def __get_loan(self, account_number: str):
        for loan in self.loans:
            if loan.account.account_number == account_number:
                if loan.status == 'active':
                    return loan
                else:
                    return False

    def __show(self, loan: Loan):
        print('LOAN ID: ', loan.id, '\n', 'DATE COLLECTED: ', loan.date, '\n', 'LOAN BALANCE: ', loan.balance, '\n', 'LOAN TYPE: ', loan.loan_type) 