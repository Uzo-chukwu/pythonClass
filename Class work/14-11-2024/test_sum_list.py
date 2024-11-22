import unittest
import sum_list

class TestSumList(unittest.TestCase):

	def test_that_sum_list_function_returns_correct_value(self):
		number =[1,2,3,4,5]
		actual = sum_list.get_sum(number)
		expected = 15
		self.assertEqual(actual, expected)


class TestRemoveFunction(unittest.TestCase):
	
	def test_that_remove_function_returns_correct_value(self):
		number =[1,2,3,4,5]
		actual = sum_list.remove_function(number)
		expected = [1,3,4,5]
		
		num =[3]
		actual = sum_list.remove_function(num)
		expected = 0
		


		self.assertEqual(actual, expected)



