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
