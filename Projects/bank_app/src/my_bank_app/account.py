class Account:
    balance = 0
    def __init__(self, name,account_number,pin):
        self.name = name
        self.account_number = account_number
        self.pin = pin



    def __get_name__(self):
        return self.name

    def __get_account_number__(self):
        return self.account_number

    def __get_balance__(self):
        return self.balance

    def __validate_pin__(self,pin):
        if pin == self.pin:
            return True
        return False

    def raise_negative_amount_error(self,amount):
        if amount < 0:
            raise ValueError("negative amount")
        return




    def increase_balance(self,amount):
        self.raise_negative_amount_error(amount)
        self.balance+= amount

    def decrease_balance(self,amount,pin):
        self.raise_negative_amount_error(amount)
        if pin == self.pin:
            if self.balance >= amount: self.balance -= amount
            else: raise ValueError("insufficient balance")
        else: raise ValueError("wrong pin")

    def change_pin(self,old_pin,new_pin):
        if old_pin == self.pin:
            self.pin = new_pin
