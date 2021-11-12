from models.AccountHolder import AccountHolder
from typing import List


class AccountHolderManager:
    account_holders: List[AccountHolder] = []

    def create_account_holder(self, email: str, password: str, confirm_password: str, first_name: str, last_name=None, phone=None,
                              middle_name=None):
        # checks if the password is correct
        if password == confirm_password:
            # getting id for an account Holder
            owner_id = self.__get_id()
            # creating an instance of Account Holder
            owner = AccountHolder(id=owner_id, email=email,
                                  first_name=first_name, password=password, )
            owner.last_name = last_name
            owner.middle_name = middle_name
            owner.phone = phone
            self.account_holders.append(owner)
            return True
        else:
            return False

    def update_account_holder(self, email: str, first_name: str, last_name: str, phone: str, middle_name: str):
        # Find the account_holder to be edited
        account_holder = self.__find(email)
        # checks if account holder is not None, edits the account holder and return True!
        if account_holder is not None:
            account_holder.first_name = first_name
            account_holder.last_name = last_name
            account_holder.middle_name = middle_name
            account_holder.phone = phone
            return True
        else:
            return False

    def list_account_holders(self):
        # Print all account_holder
        for account_holder in self.account_holders:
            self.__show(account_holder)

    def delete_account_holder(self, email: str):
        # Find the account_holder to be deleted
        account_holder = self.__find(email)
        if account_holder is None:
            return False
        else:
            # Deletes the account holder from the account holder list
            self.account_holders.remove(account_holder)
            return True

    def search(self, email: str):
        # search and returns the account holder if not None
        account_holder = self.__find(email)
        if account_holder is None:
            return False
        else:
            self.__show(account_holder)

    def login(self, email: str, password: str):
        # verify if the person trying to access an account is the owner
        for account_holder in self.account_holders:
            if account_holder.email == email and account_holder.password == password:
                return account_holder
            else:
                return False

    def change_password(self, email: str, new_password: str):
        account_holder = self.__find(email)
        if account_holder != None:
            account_holder.password = new_password
            return True
        else:
            return False

    def __get_id(self):
        # gets the length of the account holder list and try to return the length + 1 as id if the account holder
        # list is not empty a private function
        length = len(self.account_holders)
        if length == 0:
            length += 1
            return length
        else:
            for account_holder in self.account_holders:
                if account_holder.id == length:
                    length += 1
                    return length
                else:
                    continue

    def __find(self, email: str):
        # Finds the account holder by the given email in the account holder list a private function
        for account_holder in self.account_holders:
            if account_holder.email == email:
                return account_holder
            else:
                return None

    def __show(self, account_holder: AccountHolder):
        # prints an account holder information a private function
        print(account_holder.id, '.', ' ', account_holder.first_name, ' ', account_holder.middle_name,
              ' ', account_holder.last_name, '\t', account_holder.email, '\t', account_holder.phone)
