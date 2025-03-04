from src.StudentCourseManagementSystem.user import User

class Student(User):
    courses = []
    def __init__(self, user_name, user_id, email, password, ):
        super().__init__(user_name, user_id, email, password)


    def enroll_course(self, course_of_choice,courses):
        for course in courses:
            if course_of_choice == course.course_of_choice:
                self.courses.append(course)

    def view_courses_enrolled(self):
        for course in self.courses:
            print(course.get_course_title)

    def view_grades(self, courses):
        grades = {}
        for course in courses:
            grades[course.course_of_choice] = course.get_grade(self)
        return grades

