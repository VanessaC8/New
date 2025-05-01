# This will be an online banking program. This requiers a user to need an account number and a pin to identify
# themself as the owner of the account .Once they get into the system they will have the standerd options:
# 1. Check balance
# 2. Deposit
# 3. Withdraw
# # Additional options:
# 4. Create a new account
# 5. close an account 
# 6. Modify account details


  

# This function will be used to enter the pin 
def enter_pin():
    for account in Table.accounts:
        if account["pin"] == pin:
            pin = input("Enter your pin: ")
            return pin
        else:
            print("Invalid pin")
            return None
    
# This function will be used to enter the account number
def enter_account_number():
    for account in Table.accounts:
        if account["account number"] == account_number:
            account_number = input("Enter your account number: ")
            return account_number
        else:
            print("Invalid account number")
            return None

# This function will be used to select the user options
def user_seleciton():
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Create a new account")
    print("5. Close an account")
    print("6. Modify account details")
    user_selection = input("Enter your selection: ")
    return user_selection

# This function will be used to run the main program
def main():
    print("Welcome to the online banking system")
    account_number = enter_account_number()
    if enter_account_number(account_number):
        pin = enter_pin()
        if enter_pin(pin):
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

# This function will be used to check the balance
def check_balance():
    # This will be a placeholder for the actual balance
    balance = 1000
    print("Your balance is: ", balance)

# This function will be used to deposit money into the account
def deposit():
    amount = input("Enter the amount to deposit: ")
    # This will be a placeholder for the actual deposit
    print("Deposited: ", amount)
    # This will be a placeholder for the actual balance
    balance = 1000
    balance += int(amount)
    print("Your new balance is: ", balance)

# This function will be used to withdraw money from the account
def withdraw():
    amount = input("Enter the amount to withdraw: ")
    # This will be a placeholder for the actual withdraw
    print("Withdrawn: ", amount)
    # This will be a placeholder for the actual balance
    balance = 1000
    balance -= int(amount)
    print("Your new balance is: ", balance)

# This function will be used to create a new account
def create_account():
    account_number = input("Enter your new account number: ")
    pin = input("Enter your new pin: ")
    # This will be a placeholder for the actual account creation
    print("Account created with account number: ", account_number)
    print("Your new pin is: ", pin)

# This function will be used to change the account details
def modify_account_details():
    account_number = input("Enter your account number: ")
    # This will be a placeholder for the actual account modification
    print("Account modified with account number: ", account_number)

# This will be the main function to run the program
if __name__ == "__main__":
    main()
