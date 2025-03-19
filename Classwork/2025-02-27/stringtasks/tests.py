import unittest
from stringtasks import main


class MyTestCase(unittest.TestCase):
    def test_that_uppercase_first_works(self):
        actual = main.uppercase_first("aBcDeFgH")
        expected = "BDFHaceg"
        self.assertEqual(actual, expected)

    def test_that_get_number_of_occurences(self ):
        actual = main.get_number_of_occurences("semicolon","o")
        expected = ['o', 2]
        self.assertEqual(actual, expected)

    def test_that_removespecial_characters_works(self):
        actual = main.removespecial_characters("!@#$%^&*()abcd#$%%^&*()")
        expected = "abcd"
        self.assertEqual(actual, expected)

    def test_that_merge_and_swap_works(self):
        actual = main.merge_and_swap("abc","xyz")
        expected = "cba zyx"
        self.assertEqual(actual, expected)

    def test_that_character_frequency_works(self):
        actual = main.character_frequency("semicolon")
        expected = {'s': 1, 'e': 1, 'm': 1, 'i': 1, 'c': 1, 'o': 2, 'l': 1, 'n': 1}
        self.assertEqual(actual, expected)

    def test_that_put_ce_in_the_middle(self ):
        actual = main.put_ce_in_the_middle("joy")
        expected = "joyce"
        self.assertEqual(actual, expected)
        actual = main.put_ce_in_the_middle("grow")
        expected = "grceow                                                                                                                          "



if __name__ == '__main__':
    unittest.main()
