# This will be an online banking program. This requiers a user to need an account number and a pin to identify
# themself as the owner of the account .Once they get into the system they will have the standerd options:
# 1. Check balance
# 2. Deposit
# 3. Withdraw
# # Additional options:
# 4. Create a new account
# 5. close an account 
# 6. Modify account details



  


def enter_pin():
    """
    Function to enter the pin for the account
    """
    pin = input("Enter your pin: ")
    return pin

def pin_validation(pin):
    """
    Function to validate the pin for the account
    """
    # This will be a placeholder for the actual pin validation
    if pin == "1234":
        return True
    else:
        print("Invalid pin")
        return False
    

def enter_account_number():
    """
    Function to enter the account number for the account
    """
    account_number = input("Enter your account number: ")
    return account_number

def account_number_validation(account_number):
    """
    Function to validate the account number for the account
    """
    # This will be a placeholder for the actual account number validation
    if account_number == "123456789":
        return True
    else:
        print("Invalid account number")
        return False

def user_seleciton():
    """
    Function to enter the user selection for the account
    """
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Create a new account")
    print("5. Close an account")
    print("6. Modify account details")
    user_selection = input("Enter your selection: ")
    return user_selection

def main():
    """
    Main function to run the program
    """
    print("Welcome to the online banking system")
    account_number = enter_account_number()
    if account_number_validation(account_number):
        pin = enter_pin()
        if pin_validation(pin):
            while True:
                user_selection = user_seleciton()
                if user_selection == "1":
                    check_balance()
                elif user_selection == "2":
                    deposit()
                elif user_selection == "3":
                    withdraw()
                elif user_selection == "4":
                    create_account()
                elif user_selection == "5":
                    print("Closing account...")
                    # This will be a placeholder for the actual account closure
                    print("Account closed")
                    break
                elif user_selection == "6":
                    modify_account_details()
                else:
                    print("Invalid selection")
        else:
            print("Invalid pin")
    else:
        print("Invalid account number")


def check_balance():
    """
    Function to check the balance of the account
    """
    # This will be a placeholder for the actual balance
    balance = 1000
    print("Your balance is: ", balance)

def deposit():
    """
    Function to deposit money into the account
    """
    amount = input("Enter the amount to deposit: ")
    # This will be a placeholder for the actual deposit
    print("Deposited: ", amount)
    # This will be a placeholder for the actual balance
    balance = 1000
    balance += int(amount)
    print("Your new balance is: ", balance)

def withdraw():
    """
    Function to withdraw money from the account
    """
    amount = input("Enter the amount to withdraw: ")
    # This will be a placeholder for the actual withdraw
    print("Withdrawn: ", amount)
    # This will be a placeholder for the actual balance
    balance = 1000
    balance -= int(amount)
    print("Your new balance is: ", balance)


def create_account():
    """
    Function to create a new account
    """
    account_number = input("Enter your new account number: ")
    pin = input("Enter your new pin: ")
    # This will be a placeholder for the actual account creation
    print("Account created with account number: ", account_number)
    print("Your new pin is: ", pin)

def modify_account_details():
    """
    Function to modify account details
    """
    account_number = input("Enter your account number: ")
    # This will be a placeholder for the actual account modification
    print("Account modified with account number: ", account_number)

# This will be the main function to run the program
if __name__ == "__main__":
    main()
