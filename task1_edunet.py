# SIMPLE ATM INTERFACE

accounts = [
    {"account_number": 123, "pin": 1234, "balance": 15000.80},
    {"account_number": 124, "pin": 1243, "balance": 1200.0},
]

def find_account(account_number):
    for account in accounts:
        if account["account_number"] == account_number:
            return account
    return None

def validate_pin(account):
    entered_pin = int(input("Enter your PIN: "))
    return entered_pin == account["pin"]

def withdraw(account):
    try:
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= 0 or amount > account["balance"]:
            print("Please enter a valid amount.")
        else:
            account["balance"] -= amount
            print("Withdrawal successful for the amount: ", amount)
            print("New Balance: ", account["balance"])
    except ValueError:
        print("Please enter a valid number.")

def deposit(account):
    try:
        amount = float(input("Enter the amount to deposit: "))
        if amount <= 0:
            print("Please enter a valid amount.")
        else:
            account["balance"] += amount
            print("Deposit successful for the amount: ", amount)
            print("New Balance: ", account["balance"])
    except ValueError:
        print("Please enter a valid number.")

def balance_enquiry(account):
    print("Current balance : ",account['balance'])

def set_pin(account):
    existing_pin = int(input("Enter your existing 4-digit PIN: "))
    if existing_pin != account["pin"]:
        print("Incorrect PIN.")
        return
    try:
        new_pin = int(input("Enter a new 4-digit PIN: "))
        if 1000 <= new_pin <= 9999:
            account["pin"] = new_pin
            print("PIN successfully set!")
        else:
            print("Invalid PIN. Must be a 4-digit number.")
    except ValueError:
        print("Invalid PIN. Please enter a valid 4-digit number.")

while True:
    account_number = int(input("Enter your account number: "))
    
    
    if account_number == 0:
        print("ATM is now closing.")
        break

    account = find_account(account_number)
    if not account:
        print("Account not found. Try Again")
        continue
    if not validate_pin(account):
        print("Incorrect PIN. Try Again")
        continue

    # Continuous display of menu
    while True:
        print("\n1. Withdraw\n2. Deposit\n3. Balance Enquiry\n4. PIN Generation\n5. Exit")
        try:
            choice = int(input("Select an option: "))
            if choice not in range(1, 6):
                print("Invalid choice. Try again.")
                continue
            if choice == 1:
                withdraw(account)
            elif choice == 2:
                deposit(account)
            elif choice == 3:
                balance_enquiry(account)
            elif choice == 4:
                set_pin(account)
            elif choice == 5:
                print("Exiting out of ATM!")
                break
        except ValueError:
            print("Please enter a valid option.")

   
