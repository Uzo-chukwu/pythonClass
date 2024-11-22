import unittest
import sumnumber



class TestGetNumber(unittest.TestCase):

	def test_that_getnumber_returns_correct_value(self):
		
		number = [1,2,3,4,5]

		actual = sumnumber.get_number(number)

		expected = 60     
		self.assertEqual(actual, expected)

class TestMergeAndSort(unittest.TestCase):

	def test_that_merge_and_sort_returns_correct_value(self):
		
		number1 = [1,2,3,4,9]
		number2 = [5,6,7,8,12]

		actual = sumnumber.merge_and_sort(number1,number2)

		expected = [1,2,3,4,5,6,7,8,9,12]     
		self.assertEqual(actual, expected)

class TestGetVowels(unittest.TestCase):

	def test_that_getvowels_returns_correct_value(self):
		strings = "I love python"

		actual = sumnumber.getvowels(strings)

		expected = 4    
		self.assertEqual(actual, expected)

class TestGetAnagram(unittest.TestCase):

	def test_that_getanagram_returns_correct_value(self):
		first = "silent"
		second = "listen"

		actual = sumnumber.getanagram(first, second)

		expected = "True"    
		self.assertEqual(actual, expected)

class TestGetEvenNumbers(unittest.TestCase):

	def test_that_getevennumbers_returns_correct_value(self):
		numbers = [1,2,3,4,5,6]

		actual = sumnumber.getevennumber(numbers)

		expected = 12    
		self.assertEqual(actual, expected)

class TestGetPrime(unittest.TestCase):

	def test_that_getprime_returns_correct_value(self):
		number = 7

		actual = sumnumber.getprime(number)

		expected = True   
		self.assertEqual(actual, expected)

class TestGetPalindrome(unittest.TestCase):

	def test_that_getpalindrome_returns_correct_value(self):
		string = "madam"

		actual = sumnumber.getpalindrome(string)

		expected = True   
		self.assertEqual(actual, expected)

class TestGetAverage(unittest.TestCase):

	def test_that_getaverage_returns_correct_value(self):
		numbers = [1,2,3,4,5,]

		actual = sumnumber.getaverage(numbers)

		expected = 3    
		self.assertEqual(actual, expected)

class TestGetReverse(unittest.TestCase):

	def test_that_getreverse_returns_correct_value(self):
		string = "hello"

		actual = sumnumber.getreverse(string)

		expected = "olleh" 
		self.assertEqual(actual, expected)

class TestGetUppercase(unittest.TestCase):

	def test_that_getuppercase_returns_correct_value(self):
		string = ['apple','banana','oranges']

		actual = sumnumber.getuppercase(string)

		expected = ['Apple','Banana','Oranges'] 
		self.assertEqual(actual, expected)

class TestGetDuplicate(unittest.TestCase):

	def test_that_getduplicate_returns_correct_value(self):
		numbers = [1,2,3,4,5,5,6]

		actual = sumnumber.getduplicate(numbers)

		expected = True
		self.assertEqual(actual, expected)

		

class TestRemoveSpace(unittest.TestCase):

	def test_that_remove_spaces_returns_correct_value(self):
		string = 'hello   world'

		actual = sumnumber.removespace(string)

		expected = 'helloworld'
		self.assertEqual(actual, expected)

class TestGetCommonNumber(unittest.TestCase):

	def test_that_get_common_number_returns_correct_value(self):
		
		number1 = [1,2,3,4,9]
		number2 = [5,6,7,1,2,3]

		actual = sumnumber.getcommonnumber(number1,number2)

		expected = [1,2,3]     
		self.assertEqual(actual, expected)

class TestSortString(unittest.TestCase):

	def test_that_sort_string_returns_correct_value(self):
		string = ['apple','zadd','on']

		actual = sumnumber.sortstring(string)

		expected = ['on','zadd','apple'] 
		self.assertEqual(actual, expected)

class TestGetFactorial(unittest.TestCase):

	def test_that_getfactorial_returns_correct_value(self):
		number = 5

		actual = sumnumber.getfactorial(number)

		expected = 120  
		self.assertEqual(actual, expected)

class TestGetSumOfDigits(unittest.TestCase):

	def test_that_get_sum_of_digits_returns_correct_value(self):
		number = 2222

		actual = sumnumber.getsumofdigits(number)

		expected = 8
		self.assertEqual(actual, expected)

class TestGetSumOfOddDigits(unittest.TestCase):

	def test_that_get_sum_of_odd_digits_returns_correct_value(self):
		number = 1234

		actual = sumnumber.getsumofodddigits(number)

		expected = 4
		self.assertEqual(actual, expected)

class TestGetAcronym(unittest.TestCase):

	def test_that_get_acronym_returns_correct_value(self):
		string = 'nigeria bar association'

		actual = sumnumber.removespace(string)

		expected = 'NBA'
		self.assertEqual(actual, expected)

