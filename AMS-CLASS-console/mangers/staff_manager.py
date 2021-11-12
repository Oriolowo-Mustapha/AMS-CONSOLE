from models.Manager import Manager
from models.Account import Account
from typing import List

class staff:

    staffs: List[Manager] = []

    def register_staff(self, email: str, password: str, confirm_password: str, first_name: str, last_name=None, phone=None,middle_name=None):
        if password == confirm_password:
            # getting id for an account Holder
            owner_id = self.__get_id()
            # creating an instance of Account Holder
            owner = staff(id=owner_id, email=email,
                                  first_name=first_name, password=password, )
            owner.last_name = last_name
            owner.middle_name = middle_name
            owner.phone = phone
            self.staffs.append(owner)
            return True
        else:
            return False

    
    def login(self, email: str, password: str):
        # verify if the person trying to access an account is the owner
        for staff in self.staffs:
            if staff.email == email and staff.password == password:
                return staff
            else:
                return False
    
    def block_account(self, email: str):
        account_status = "active"
        find_staff = self.__find(email)
        if find_staff is not None:
            account_status = "inactive"
            return True
        else:
            return False

    def unblock_account(self, email: str):
        account_status = "inactive"
        find_staff = self.__find(email)
        if find_staff is not None:
            account_status = "active"
            return True
        else:
            return False

    def list_accounthol(self):
        for staff in self.staffs:
            self.__show(staff)

    def search_account(self, email:str):
        staff = self.__find(email)
        if staff is None:
            return False
        else:
            self.__show(staff)
            
            

    def __get_id(self):
        # gets the length of the account holder list and try to return the length + 1 as id if the account holder
        # list is not empty a private function
        length = len(self.staffs)
        if length == 0:
            length += 1
            return length
        else:
            for staff in self.staffs:
                if staff.id == length:
                    length += 1
                    return length
                else:
                    continue

    def __find(self, email: str):
        # Finds the account holder by the given email in the account holder list a private function
        for staff in self.staffs:
            if staff.email == email:
                return staff
            else:
                return None