from mangers.LoanManager import LoanManager
from models.AccountHolder import AccountHolder
from mangers.AccountHolderManager import AccountHolderManager
from models.Loan import Loan
from mangers.staff_manager import staff

acount_holder_manager = AccountHolderManager()
staff_manager = staff

bank_name = "Musti's Bank"
main_menu_opt = ["0. QUIT", "1. ACCOUNT HOLDER MENU", "2. MANAGER MENU"]
acc_hol_menu = ["0. GO BACK", "1. REGISTER AN ACCOUNT WITH US", "2. UPDATE YOUR ACCOUNT DETAILS", "3. CHANGE PASSWORD", "4. OBTAIN LOAN", "5. OBTAIN OVERDRAFT"]
man_menu = ["0. GO BACK", "1. REGISTER AS A MANAGER", "2. LOGIN AS A MANAGER", "3. BLOCK AN ACCOUNT", "4. LIST ALL THE ACCOUNT HOLDERS", "5. SEARCH AN ACCOUNT", "6. UNBLOCK AN ACCOUNT"]

def mainMenu():
    print("Welcome to", bank_name)
    for i in main_menu_opt:
        print(i) 


def show_sub_menu(option):
    if option == 0:
        print('Thank you for using', bank_name)
    elif option == 1:
        show_account_holder_menu()
        action = int(input())
        if action == 0:
            mainMenu()
        else:
            handle_account_holder_menu(action)
    elif option == 2:
        show_manager_menu()
        action = int(input())
        if action == 0:
            mainMenu()
        else:
            handle_manager(action)
            

def show_account_holder_menu():
    for u in acc_hol_menu:
        print(u)

def show_manager_menu():
    for e in man_menu:
        print(e)

def handle_account_holder_menu(action):
    if action == 1:
        email = str(input('Enter your email address: '))
        password = str(input('Enter Your password: '))
        confirm_password = str(input('Confirm your password: '))
        first_name = str(input(
            'Enter your first name: '))
        last_name = str(input(
            'Enter your last name' '\t' 'if the last name is not given None will be used: '))
        middle_name = str(input(
            'Enter your middle name' '\t' 'if the middle name is not given None will be used: '))
        phone = str(input(
            'Enter your phone number' '\t' 'if phone number is not given None will be used: '))
        holder = acount_holder_manager.create_account_holder(
            email=email, password=password, confirm_password=confirm_password, first_name=first_name, last_name=last_name, phone=phone, middle_name=middle_name)
        if holder is True:
            print(
                'Congrats Your account have been created' '\t' 'Your password is your first name')
            request1 = str(input("Do you want to go to the mainmenu  (YN): "))
            if request1 == "Y":
                for o in acc_hol_menu:
                    print(o)
            else:
                print("THANKS FOR USING", bank_name)
        else:
            print('Password is incorrect')

    elif action == 2:
        email = str(input('Enter your email address: '))
        password = str(input('Enter Your password: '))
        holder = acount_holder_manager.login(email=email, password=password)
        if holder is False:
            print('Email or password incorrect')
        else:
            first_name = str(input(
                'Enter your first name'))
            last_name = str(input(
                'Enter your last name' '\t' 'if the last name is not given None will be used: '))
            middle_name = str(input(
                'Enter your middle name' '\t' 'if the middle name is not given None will be used: '))
            phone = str(input(
                'Enter your phone number' '\t' 'if phone number is not given None will be used: '))
            new_holder = acount_holder_manager.update_account_holder(
                email=email, first_name=first_name, last_name=last_name, phone=phone, middle_name=middle_name)
            if new_holder is True:
                print('Update valid')
            else:
                print('Update invalid')

    elif action == 3:
        email = str(input('Enter your email address: '))
        new_password = str(input('Enter the new password: '))
        status = acount_holder_manager.change_password(
            email=email, new_password=new_password)
        if status is True:
            print('Password is valid')
        else:
            print('information invaid')

    elif action == 4:
        loan_types = ["0. GO BACK" , "1. HOUSEHOLD FEE", "2. CAR FEE", "3. SCHOOL FEE", "4. BUISENESS FEE", "5. EMERGENCY FEE"]
        for r in loan_types:
            print(r)
        email = 'Enter your email address: '
        print(email)
        request2 = (str(input("")))
     
        num_of_months = (int(input("Enter the number of month you want to pay: ")))
        loan_holder = LoanManager.create_loan(email=email, loan_type= request2, number_of_months=num_of_months)
        if loan_holder == True:
           print("LOAN GRANTED")
        else:
            print("LOAN NOT GARNTED PLEASE PAY UP YOUR LOAN DEPTH")


            
            
# MANAGER MENU
def handle_manager(action):
    if action == 1:
        email = str(input("Enter your email: "))
        password = str(input('Enter Your password: '))
        confirm_password = str(input('Confirm your password: '))
        first_name = str(input(
            'Enter your first name: '))
        last_name = str(input(
            'Enter your last name' '\t' 'if the last name is not given None will be used: '))
        middle_name = str(input(
            'Enter your middle name' '\t' 'if the middle name is not given None will be used: '))
        phone = str(input(
            'Enter your phone number' '\t' 'if phone number is not given None will be used: '))

        staff = staff_manager.register_staff(email= email, password=password, confirm_password= confirm_password, first_name=first_name, last_name=last_name, phone = phone, middle_name=middle_name)
        if staff == True:
            print("ACCOUNT SUCCESSFULLY CREATED")
        else:
            print("PLEASE CHECK YOUR PASSWORD")

    elif action == 2:
        email = str(input("Enter your email: "))
        password = str(input('Enter Your password: '))
        staf = staff_manager.login(email=email, password=password)
        if staf == True:
            print("LOGIN SUCCESSFUL")
        else:
            print("NO ACTIVE ACCOUNT")
    
    elif action == 3:
        email = str(input("Enter the email of the account you want to block: "))
        blocker = staff_manager.block_account(email=email)
        if blocker == True:
            print('ACCOUNT BLOCKED')
        else:
            print("ACCOUNT NOT BLOCKED")
    
    elif action == 4:
        list=acount_holder_manager.list_account_holders()
        print(list)

    elif action == 5:
        email = str(input('Enter your email address: '))
        holder = acount_holder_manager.search(email=email)
        if holder is False:
            print('ACCOUNT Not Found')
        else:
            show = acount_holder_manager.__show()
            print(show)

    elif action == 6:
        email = str(input('Enter the email address you want to unblock: '))
        unblock = staff_manager.unblock_account(email=email)
        if unblock == True:
            print("ACCOUNT UNBLOCKED")
        else:
            print("ACCOUNT NOT UNBLOCKED")


   


    show_sub_menu(1)


def main():
    rerun = True
    while(rerun):
        mainMenu()
        option = int(input())
        if(option == 0):
            rerun = False
        else:
            show_sub_menu(option)


main()
