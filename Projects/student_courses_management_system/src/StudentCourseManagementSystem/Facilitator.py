from src.Course import Course
from src.StudentCourseManagementSystem.user import User


class Facilitator(User):

    course = []
    def __init__(self, user_name, user_id, email, password):
        super().__init__(user_name, user_id, email, password)

    def create_course(cls, course_title, course_code):
        new_course = Course(cls, course_title, course_code)
        cls.course.append(new_course)

    @classmethod
    def get_courses(cls):
        return cls.course

    def get_course_size(cls):
        return len(cls.course)
# course = Course("Python", 101)
# course.create_course(cls, course_title, course_code)

# print(course.get_course_size())


