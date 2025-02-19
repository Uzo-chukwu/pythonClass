import unittest
import function

class TestDivideOrSquare(unittest.TestCase):

	def test_that_divide_or_square_function_exists(self):
		function.divide_or_square(4)

	def test_that_divide_or_square_function_returns_correct_value(self):
		actual = function.divide_or_square(12)
		expected = 2     
		self.assertEqual(actual, expected)
		actual = function.divide_or_square(25)
		expected = 5
		self.assertEqual(actual, expected)
	
	def test_that_divide_or_square_function_works_with_negative_numbers(self):
		actual = function.divide_or_square(-12)
		expected = 3   
		self.assertEqual(actual, expected)
		actual = function.divide_or_square(-25)
		expected = 5
		self.assertEqual(actual, expected)

	def test_that_divide_or_square_function_works_with_float_numbers(self):
		actual = function.divide_or_square(12.5)
		expected = 2.5
		self.assertEqual(actual, expected)
		actual = function.divide_or_square(25.5)
		expected = 0.5
		self.assertEqual(actual, expected)

	def test_that_divide_or_square_function_works_with_large_numbers(self):
		actual = function.divide_or_square(1000000)
		expected = 1000
		self.assertEqual(actual, expected)
		actual = function.divide_or_square(99999999)
		expected = 4
		self.assertEqual(actual, expected)

	def test_that_divide_or_square_function_works_with_numbers_less_than_one(self):
		actual = function.divide_or_square(0.9)
		expected = 0.9
		self.assertEqual(actual, expected)
		actual = function.divide_or_square(0.5)
		expected = 0.5
		self.assertEqual(actual, expected)

	def test_that_divide_or_square_function_raise_exception_with_invalid_input(self):
		self.assertRaises(TypeError, function.divide_or_square, "erorr")


class GetFutureInvestmentValue(unittest.TestCase):
	
	def test_that_get_future_investment_value_function_exists(self):
		function.get_future_investment_value(1000,8,2)
	
	def test_that_get_future_investment_value_function_returns_correct_value(self):
		actual = function.get_future_investment_value(1000,8,2)
		expected = 5
		self.assertEqual(actual, expected)


class GetOnlyFloats(unittest.TestCase):
	
	def test_that_get_only_floats_function_exist(self):
		function.get_only_floats(1,2)



		