from bank_app.src.my_bank_app.bank import Bank

bank = Bank()
def create_account():
    name = input("Enter your name: ")
    account_number = input("Enter your account number: ")
    pin = input("Enter your pin: ")
    bank.create_account(name, account_number, pin)

def check_balance():
    account_number = input("Enter your account number: ")
    pin = input("Enter your pin: ")
    balance = bank.get_balance(account_number, pin)
    print("Your balance is:", balance)

def deposit():
    account_number = input("Enter your account number: ")
    amount = float(input("Enter your amount: "))
    bank.deposit(account_number, amount)
    print("deposit successful")

def withdraw():
    account_number = input("Enter your account number: ")
    amount = float(input("Enter your amount: "))
    pin = input("Enter your pin: ")
    bank.withdraw(account_number, amount, pin)
    print("withdrawal successful")

def transfer_money():
    sender_account_number = input("Enter your account number: ")
    recipient_account_number = input("Enter receiver's account number: ")
    amount = float(input("Enter your amount: "))
    pin = input("Enter your pin: ")
    bank.transfer_money(sender_account_number, recipient_account_number, amount, pin)
    print("transfer successful")

def update_pin():
    account_number = input("Enter your account number: ")
    old_pin = input("Enter your old pin : ")
    new_pin = input("Enter your new pin : ")
    bank.update_pin(account_number, old_pin, new_pin)
    print("pin updated successful")

def main():
    print("Welcome to Bank App")

    print("""
        1. Create Account
        2. Check balance
        3. Deposit
        4. Withdraw
        5. Transfer Money
        6. Update Pin
        7. Exit
    """)
    while True:
      choice = (input("Enter your choice: "))
      match choice:
          case "1":
            create_account()
          case "2":
              check_balance()
          case "3":
              deposit()
          case "4":
              withdraw()
          case "5":
              transfer_money()
          case "6":
              update_pin()
          case "7":
              break

main()
