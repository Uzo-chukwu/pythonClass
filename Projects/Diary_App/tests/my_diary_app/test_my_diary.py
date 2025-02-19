import unittest
from datetime import datetime

from diary import Diary
from my_diary_app.entry import Entry

class EntryTestCase(unittest.TestCase):
    def setUp(self):
        self.entry = Entry("Title","Body",1)
    def test_get_title(self):
        actual = self.entry.get_title()
        expected = "Title"
        self.assertEqual(actual, expected)

    def test_get_body(self):
        actual = self.entry.get_body()
        expected = "Body"
        self.assertEqual(actual, expected)

    def test_get_id(self):
        actual = self.entry.get_id()
        expected = 1
        self.assertEqual(actual, expected)

    def test_set_id(self):
        self.entry.set_id(2)
        actual = self.entry.get_id()
        expected = 2
        self.assertEqual(actual, expected)

    def test_set_title(self):
        self.entry.set_title("Another title")
        actual = self.entry.get_title()
        expected = "Another title"
        self.assertEqual(actual, expected)

    def test_set_body(self):
        self.entry.set_body("Another body")
        actual = self.entry.get_body()
        expected = "Another body"
        self.assertEqual(actual, expected)

class DiaryTestCase(unittest.TestCase):
    def setUp(self):
        self.diary = Diary("username","password")

    def test_get_username(self):
        actual = self.diary.get_username()
        expected = "username"
        self.assertEqual(actual, expected)




if __name__ == '__main__':
    unittest.main()
