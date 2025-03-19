import unittest
import function

class TestGetSumOfEvenNumbers(unittest.TestCase):

	def test_that_get_sum_of_even_numbers_function_exists(self):
		numbers = [1,2,3,4,5,6]
		function.get_sum_of_even_numbers(numbers)

	def test_that_get_sum_of_even_numbers_function_returns_correct_value(self):
		numbers = [1,2,3,4,5,6]

		actual = function.get_sum_of_even_numbers(numbers)
		expected = 12     
		self.assertEqual(actual, expected)
		

class TestGetPrimeNumberBefore(unittest.TestCase):

	def test_that_get_get_prime_number_before_function_exists(self):
		number = 19
		function.get_prime_number_before(number)

	def test_that_get_prime_number_before_function_returns_correct_value(self):
		number = 7

		actual = function.get_prime_number_before(number)
		expected = [2,3,5]     
		self.assertEqual(actual, expected)

class TestGetEvenNumberCount(unittest.TestCase):

	def test_that_get_even_number_count_function_exists(self):
		numbers = [1,2,3,4]
		function.get_even_number_count(numbers)

	def test_that_get_even_number_count_function_returns_correct_value(self):
		numbers = [1,2,3,4]

		actual = function.get_even_number_count(numbers)
		expected = 2    
		self.assertEqual(actual, expected)

class TestGetBooleanValue(unittest.TestCase):

	def test_that_get_boolean_value_function_exists(self):
		numbers = [1,2,3,4]
		function.get_boolean_value(numbers)

	def test_that_get_boolean_value_function_returns_correct_value(self):
		numbers = [1,2,3,4]

		actual = function.get_boolean_value(numbers)
		expected = [False,True,False,True]    
		self.assertEqual(actual, expected)


class TestCapitalizeFirstLetter(unittest.TestCase):

	def test_that_capitalize_first_Letter_function_exists(self):
		phrase = ['red','orange','yellow','green','blue']
		function.capitalize_first_Letter(phrase)

	def test_that_capitalize_first_Letter_returns_correct_value(self):
		phrase = ['red','orange','yellow','green','blue']

		actual = function.capitalize_first_Letter(phrase)
		expected = ['Red','Orange','Yellow','Green','Blue']   
		self.assertEqual(actual, expected)


class TestMultipleOfThree(unittest.TestCase):

	def test_that_multiple_of_three_exists(self):
		number = 30
		function.multiple_of_three(number)

	def test_that_multiple_of_three_returns_correct_value(self):
		number = 30

		actual = function.multiple_of_three(number)
		expected = [3,6,9,12,15,18,21,24,27,30]   
		self.assertEqual(actual, expected)
class TestSquareOddNumbers(unittest.TestCase):

	def test_that_square_odd_numbers_exists(self):
		numbers = [1,2,3,4,5] 
		function.square_odd_numbers(numbers)

	def test_that_square_odd_numbers_returns_correct_value(self):
		numbers = [1,2,3,4,5] 

		actual = function.square_odd_numbers(numbers)
		expected = [1,9,25]   
		self.assertEqual(actual, expected)

class TestSquareNumbersBefore(unittest.TestCase):

	def test_that_sqaure_numbers_before_exists(self):
		number = 4
		function.sqaure_numbers_before(number)

	def test_that_square_odd_numbers_returns_correct_value(self):
		number = 4

		actual = function.sqaure_numbers_before(number)
		expected = [1,4,9,16]   
		self.assertEqual(actual, expected)

class TestGetNumbersGreaterThanTen(unittest.TestCase):

	def test_that_get_numbers_greater_than_ten_exists(self):
		numbers = [4,12,34,2,1,56]
		function.get_numbers_greater_than_ten(numbers)

	def test_that_get_numbers_greater_than_ten_returns_correct_value(self):
		numbers = [4,12,34,2,1,56]

		actual = function.get_numbers_greater_than_ten(numbers)
		expected = [12,34,56]   
		self.assertEqual(actual, expected)

class TestCheckPalindrome(unittest.TestCase):

	def test_that_check_palindrome_exists(self):
		words = ["madam","apple","racecar"]
		function.check_palindrome(words)

	def test_that_check_palindrome_returns_correct_value(self):
		words = ["madam","apple","racecar"]

		actual = function.check_palindrome(words)
		expected = [True,False,True]   
		self.assertEqual(actual, expected)
"""
class TestGetInt(unittest.TestCase):

	def test_that_get_int_exists(self):
		nonsense = "wtehdb1234"
		function.get_int(nonsense)

	def test_that_check_palindrome_returns_correct_value(self):
		nonsense = "wtehdb1234"

		actual = function.get_int(nonsense)
		expected = [1,2,3,4]   
		self.assertEqual(actual, expected)
"""
class TestAddUp(unittest.TestCase):

	def test_that_add_up_exists(self):
		number = 192374
		function.add_up(number)

	def test_that_add_up_returns_correct_value(self):
		number = 192374

		actual = function.add_up(number)
		expected = 26  
		self.assertEqual(actual, expected)


class TestGetNLetterWords(unittest.TestCase):

	def test_that_get_n_letter_words_exists(self):
		words = ["qwert","qwert","qwe","qwert"]
		number = 5
		function.get_n_letter_words(words,number)

	def test_that_get_n_letter_words_returns_correct_value(self):
		words = ["qwert","qwert","qwe","qwert"]
		number = 5


		actual = function.get_n_letter_words(words,number)
		expected = ["qwert","qwert","qwert"] 
		self.assertEqual(actual, expected)


class TestPairUpList(unittest.TestCase):

	def test_that_pair_up_list_exists(self):
		keys = ['name','age','city']
		values = ['Alice','25','Yaba']		
		function.pair_up_list(keys,values)

	def test_that_pair_up_list_returns_correct_value(self):
		keys = ['name','age','city']
		values = ['Alice','25','Yaba']	
		


		actual = function.pair_up_list(keys,values)
		expected = {'name':'Alice','age':'25','city':'Yaba'}
		self.assertEqual(actual, expected)

	def test_that_get_dict_values_exists(self):
		diction =  {'name':'Alice','age':'25','city':'Yaba'}
		function.get_dict_values(diction)

	def test_that_get_dict_values_returns_correct_value(self):
		diction =  {'name':'Alice','age':'25','city':'Yaba'}
			
		


		actual = function.get_dict_values(diction)
		expected = ['Alice','25','Yaba']
		self.assertEqual(actual, expected)

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
	                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           



