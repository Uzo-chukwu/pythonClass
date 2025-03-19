import unittest
import rot13_cipher

class TestEncryptText(unittest.TestCase):
    def test_that_encrypt_text_exixts(self):
        rot13_cipher.encrypt('abcdefg', 13)

    def test_that_encrypt_text_returns_correct_value(self):

        actual = rot13_cipher.encrypt('u 7',13)
        expected = 'h 7'
        assert actual == expected




if __name__ == '__main__':
    unittest.main()
