class Course:
    students = []
    grades = {}
    def __init__(self, course_title, course_code):
        self.__course_title = course_title
        self.__course_code = course_code

    @property
    def get_course_title(self):
        return self.__course_title
    @property
    def get_course_code(self):
        return self.__course_code

    def add_student(self, student):
        self.students.append(student)

    def grade_student(self, student, grade):
        self.grades[student.get_user_name] = grade

    def get_grade(self,student):
        return self.grades[student.get_user_name]

