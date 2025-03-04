from src.StudentCourseManagementSystem.Facilitator import Facilitator
from src.StudentCourseManagementSystem.student import Student


class Portal:
    facilitators = []
    students = []
    def __init__(self):
        pass

    def create_facilitator(self,  user_name, user_id, email, password, course_name, course_id):
        facilitator = Facilitator(user_name, user_id, email, password, course_name, course_id)
        self.facilitators.append(facilitator)

    def create_student(self, user_name, user_id, email, password, course_name, course_id):
        student = Student(user_name, user_id, email, password, course_name, course_id)
        self.students.append(student)

    def get_all_courses(self):
        courses = []
        for facilitator in self.facilitators:
            courses.append(facilitator.get_course())
        return courses


