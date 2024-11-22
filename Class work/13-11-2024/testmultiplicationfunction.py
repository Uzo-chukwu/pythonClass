	
import unittest
import multiplicationfunction

class TestMultiply(unittest.TestCase):
	def test_that_multiplication_function_exists(self):
		multiplicationfunction.multiply(2,3)

	def test_that_multiply_function_returns_correct_value(self):
		actual = multiplicationfunction.multiply(2,4)
		expected = 8      
		self.assertEqual(actual, expected)
		actual = multiplicationfunction.multiply(3,6)
		expected = 18
		self.assertEqual(actual, expected)
