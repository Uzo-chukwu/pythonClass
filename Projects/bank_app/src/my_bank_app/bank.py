from bank_app.src.my_bank_app.account import Account


class Bank:
    accounts = []
    def __init__(self):
        self.accounts = []

    def create_account(self,  name,account_number,pin):
        self.accounts.append(Account(name,account_number,pin))

    def get_number_of_accounts(self):
        return len(self.accounts)

    def deposit(self, account_number,amount):
        for account in self.accounts:
            if account.account_number == account_number:
                account.increase_balance(amount)

    def get_balance(self, account_number,pin):
        for account in self.accounts:
            if account.account_number == account_number and account.__validate_pin__(pin):
                return account.__get_balance__()
        raise ValueError("account not found")

    def withdraw(self, account_number,amount,pin):
        for account in self.accounts:
            if account.account_number == account_number:
                account.decrease_balance(amount,pin)

    def transfer(self,sender_account_number,receivers_account_number,amount,pin):
        try:
            self.withdraw(sender_account_number,amount,pin)
            self.deposit(receivers_account_number,amount)
        except ValueError as e:
            print(e)

    def update_pin(self,old_pin,new_pin):
        for account in self.accounts:
            if account.__validate_pin__(old_pin):
                account.change_pin(old_pin,new_pin)









