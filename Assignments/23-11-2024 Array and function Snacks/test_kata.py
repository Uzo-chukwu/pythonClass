import unittest
import kata

class TestGetLargestElement(unittest.TestCase):

    def test_that_get_largest_element_function_exists(self):
        kata.get_largest_element([1, 2, 3])

    def test_that_get_largest_element_function_returns_correct_value(self):
        actual = kata.get_largest_element([1, 2, 3, 4, 5])
        expected = 5
        self.assertEqual(actual, expected)
        actual = kata.get_largest_element([-1, -5, -3])
        expected = -1
        self.assertEqual(actual, expected)


class TestReverseList(unittest.TestCase):

    def test_that_reverse_list_function_exists(self):
        kata.reverse_list([1, 2, 3])

    def test_that_reverse_list_function_returns_correct_value(self):
        actual = kata.reverse_list([1, 2, 3])
        expected = [3, 2, 1]
        self.assertEqual(actual, expected)
        actual = kata.reverse_list([])
        expected = []
        self.assertEqual(actual, expected)


class TestCheckElement(unittest.TestCase):

    def test_that_check_element_function_exists(self):
        kata.check_element(3, [1, 2, 3])

    def test_that_check_element_function_returns_correct_value(self):
        actual = kata.check_element(3, [1, 2, 3])
        expected = True
        self.assertEqual(actual, expected)
        actual = kata.check_element(5, [1, 2, 3])
        expected = False
        self.assertEqual(actual, expected)


class TestPrintOddPosition(unittest.TestCase):

    def test_that_print_odd_position_function_exists(self):
        kata.print_odd_position([1, 2, 3, 4])

    # Testing output functions typically requires capturing stdout, not included here.


class TestPrintEvenPosition(unittest.TestCase):

    def test_that_print_even_position_function_exists(self):
        kata.print_even_position([1, 2, 3, 4])


class TestGetRunningTotal(unittest.TestCase):

    def test_that_get_running_total_function_exists(self):
        kata.get_running_total([1, 2, 3])

    def test_that_get_running_total_function_returns_correct_value(self):
        actual = kata.get_running_total([1, 2, 3])
        expected = 6
        self.assertEqual(actual, expected)


class TestCheckPalindrome(unittest.TestCase):

    def test_that_check_palindrome_function_exists(self):
        kata.check_palindrome("Madam")

    def test_that_check_palindrome_function_returns_correct_value(self):
        actual = kata.check_palindrome("Madam")
        expected = True
        self.assertEqual(actual, expected)
        actual = kata.check_palindrome("Hello")
        expected = False
        self.assertEqual(actual, expected)


class TestGetSumOfNumbersFor(unittest.TestCase):

    def test_that_get_sum_of_numbers_for_function_exists(self):
        kata.get_sum_of_numbers_for([1, 2, 3])

    def test_that_get_sum_of_numbers_for_function_returns_correct_value(self):
        actual = kata.get_sum_of_numbers_for([1, 2, 3])
        expected = 6
        self.assertEqual(actual, expected)


class TestGetSumOfNumbersWhile(unittest.TestCase):

    def test_that_get_sum_of_numbers_while_function_exists(self):
        kata.get_sum_of_numbers_while([1, 2, 3])

    def test_that_get_sum_of_numbers_while_function_returns_correct_value(self):
        actual = kata.get_sum_of_numbers_while([1, 2, 3])
        expected = 6
        self.assertEqual(actual, expected)


class TestGetSumOfNumbersDoWhile(unittest.TestCase):

    def test_that_get_sum_of_numbers_do_while_function_exists(self):
        kata.get_sum_of_numbers_do_while([1, 2, 3])

    def test_that_get_sum_of_numbers_do_while_function_returns_correct_value(self):
        actual = kata.get_sum_of_numbers_do_while([1, 2, 3])
        expected = 6
        self.assertEqual(actual, expected)


class TestConcatenateList(unittest.TestCase):

    def test_that_concatenate_list_function_exists(self):
        kata.concatenate_list(['a', 'b'], [1, 2])

    def test_that_concatenate_list_function_returns_correct_value(self):
        actual = kata.concatenate_list(['a', 'b'], [1, 2])
        expected = ['a', 'b', 1, 2]
        self.assertEqual(actual, expected)


class TestGetListOfDigits(unittest.TestCase):

    def test_that_get_list_of_digits_function_exists(self):
        kata.get_list_of_digits(123)

    def test_that_get_list_of_digits_function_returns_correct_value(self):
        actual = kata.get_list_of_digits(123)
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)


class TestIsEven(unittest.TestCase):

    def test_that_is_even_function_exists(self):
        kata.is_even(4)

    def test_that_is_even_function_returns_correct_value(self):
        actual = kata.is_even(4)
        expected = True
        self.assertEqual(actual, expected)
        actual = kata.is_even(3)
        expected = False
        self.assertEqual(actual, expected)


class TestIsPrimeNumber(unittest.TestCase):

    def test_that_is_prime_number_function_exists(self):
        kata.is_prime_number(5)

    def test_that_is_prime_number_function_returns_correct_value(self):
        actual = kata.is_prime_number(5)
        expected = True
        self.assertEqual(actual, expected)
        actual = kata.is_prime_number(4)
        expected = False
        self.assertEqual(actual, expected)


class TestFactorialOf(unittest.TestCase):

    def test_that_factorial_of_function_exists(self):
        kata.factorial_of(5)

    def test_that_factorial_of_function_returns_correct_value(self):
        actual = kata.factorial_of(5)
        expected = 120
        self.assertEqual(actual, expected)
        actual = kata.factorial_of(0)
        expected = 1
        self.assertEqual(actual, expected)


class TestSquareOf(unittest.TestCase):

    def test_that_square_of_function_exists(self):
        kata.square_of(3)

    def test_that_square_of_function_returns_correct_value(self):
        actual = kata.square_of(3)
        expected = 9
        self.assertEqual(actual, expected)


