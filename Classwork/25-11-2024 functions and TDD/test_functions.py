import unittest
import functions

class TestSwitchList(unittest.TestCase):

	def test_that_switch_list_function_exists(self):
		functions.switch_list([1, 2, 3,4,5],2)

	def test_that_switch_list_function_returns_correct_value(self):
		actual = functions.switch_list([1, 2, 3,4,5],2)
		expected = [1,2,4,5,3]
		self.assertEqual(actual, expected)
	
		actual = functions.switch_list([1, 2, 3,4,5],3)
		expected = [1,2,3,5,4]
		self.assertEqual(actual, expected)



class TestDivideList(unittest.TestCase):

	def test_that_divide_list_function_exists(self):
		
		functions.divide_list([1, 2, 3,4,5])

	def test_that_divide_list_function_returns_correct_value(self):
		list = [1, 2, 3,4,5]
		actual = functions.divide_list(list)
		expected = [[1,2,3],[4,5]]
		self.assertEqual(actual, expected)
	
		list = [1, 2, 3,4,5,6]
		actual = functions.divide_list(list)
		expected = [[1,2,3],[4,5,6]]
		self.assertEqual(actual, expected)



class TestCheckOddAndEvenElements(unittest.TestCase):

	def test_that_check_odd_and_even_elements_function_exists(self):
		functions.check_odd_and_even_elements([1, 2, 3,4,5])

	def test_that_check_odd_and_even_elements_function_returns_correct_value(self):
		actual = functions.check_odd_and_even_elements([1, 2, 3,4,5])
		expected = [False,True,False,True,False]
		self.assertEqual(actual, expected)
