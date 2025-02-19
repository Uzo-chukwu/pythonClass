import unittest
from bank_app.src.my_bank_app.bank import Bank


class MyTestCase(unittest.TestCase):
    def test_that_bank_exists(self):
        bank = Bank()
        self.assertEqual(bank, bank)

    def test_that_account_can_be_created(self):
            bank = Bank()
            bank.create_account("name","account number","pin")
            self.assertEqual(bank.get_number_of_accounts(),1)

    def test_that_deposit_can_be_made(self):
        bank = Bank()
        bank.create_account("name","account number","pin")
        bank.deposit("account number",1000)
        self.assertEqual(bank.get_balance("account number","pin"),1000)

    def test_that_balance_can_be_gotten(self):
        bank = Bank()
        bank.create_account("name","account number","pin")
        self.assertEqual(bank.get_balance("account number","pin"),0)


    def test_that_withdraw_can_be_made(self):
        bank = Bank()
        bank.create_account("name","account number","pin")
        bank.deposit("account number",2000)
        bank.withdraw("account number",1000,"pin")
        self.assertEqual(bank.get_balance("account number","pin"),1000)

    def test_that_transfer_can_be_made(self):
        bank = Bank()
        bank.create_account("name","account number","pin")
        bank.create_account("name1","account number2","pin2")
        bank.deposit("account number",2000)
        bank.transfer("account number","account number2",1000,"pin")
        #self.assertEqual(bank.get_balance("account number","pin"),1000)
        self.assertEqual(bank.get_balance("account number2","pin2"),1000)

    def test_that_pin_can_be_updated(self):
        bank = Bank()
        bank.create_account("name","account number","pin")
        bank.update_pin("pin","new pin")
        self.assertEqual(bank.get_balance("account number","new pin"),0)



if __name__ == '__main__':
    unittest.main()
