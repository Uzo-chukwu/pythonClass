import unittest
from src.StudentCourseManagementSystem.Facilitator import Facilitator
from src.StudentCourseManagementSystem.Admin import Admin
class AdminTest(unittest.TestCase):
    def test_admin_exists(self):
        my_admin = Admin("John", "123BD", "john123@gmail.com", "0000" )

    def test_create_admin(self):
        my_admin = Admin("John", "123BD", "john123@gmail.com", "0000")

    def test_that_facilitator_is_created_successfully(self):
        my_admin = Admin("John", "123BD", "john123@gmail.com", "0000")
        my_admin.create_facilitator("John", "123BD", "john123@gmail.com", "0000")
        self.assertEqual(my_admin.get_facilitator_size(), 1)

    def test_that_more_facilitator_created_successfully(self):
        my_admin = Admin("John", "123BD", "john123@gmail.com", "0000")
        my_admin.create_facilitator("John", "123BD", "john123@gmail.com", "0000")
        self.assertEqual(my_admin.get_facilitator_size(), 1)


        my_admin.create_facilitator("Stephen", "123BJ", "stephen123@gmail.com", "2020")
        self.assertEqual(my_admin.get_facilitator_size(), 2)

        my_admin.create_facilitator("Mark", "290GJ", "mark123@gmail.com", "2456")
        self.assertEqual(my_admin.get_facilitator_size(), 3)






