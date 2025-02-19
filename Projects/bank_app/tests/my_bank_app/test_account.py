import unittest
from bank_app.src.my_bank_app.account import Account


class MyAccountTestCase(unittest.TestCase):
    def setUp(self):
        my_account = Account("name","account number","pin")

    def test_that_account_exists(self):
        my_account = Account("name","account number","pin")

    def test_that_account_can_be_created(self):
        my_account = Account("name","account number","pin")
        self.assertEqual(my_account.__get_name__(), "name")

    def test_that_balance_is_zero_at_account_creation(self):
        my_account = Account("name","account number","pin")
        self.assertEqual(my_account.__get_balance__(), 0)
    def test_that_balance_can_be_increased(self):
        my_account = Account("name","account number","pin")
        my_account.increase_balance(1000)
        self.assertEqual(my_account.__get_balance__(), 1000)

    def test_that_attempting_to_increase_with_negative_value_throws_an_error(self):
        my_account = Account("name","account number","pin")
        self.assertRaises(ValueError, my_account.increase_balance, -1000)

    def test_that_balance_can_be_decreased(self):
        my_account = Account("name","account number","pin")
        my_account.increase_balance(1000)
        self.assertEqual(my_account.__get_balance__(), 1000)
        my_account.decrease_balance(500,"pin")
        self.assertEqual(my_account.__get_balance__(), 500)

    def test_that_attempting_to_decrease_balance_with_negative_value_throws_an_error(self):
        my_account = Account("name","account number","pin")
        self.assertRaises(ValueError, my_account.decrease_balance, -1000,"pin")

    def test_that_attempting_to_decrease_balance_with_amount_bigger_than_balance_throws_an_error(self):
        my_account = Account("name","account number","pin")
        my_account.increase_balance(100)
        self.assertEqual(my_account.__get_balance__(), 100)
        self.assertRaises(ValueError, my_account.decrease_balance, -200,"pin")



if __name__ == '__main__':
    unittest.main()
