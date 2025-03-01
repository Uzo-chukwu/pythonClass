from src.StudentCourseManagementSystem.user import User
from src.StudentCourseManagementSystem.Facilitator import Facilitator
class Admin(User):
    facilitators = []
    def __init__(self, user_name, user_id, email, password):
        super().__init__(user_name, user_id, email, password)

    @classmethod
    def facilitators_list(cls):
        return cls.facilitators

    def create_facilitator(cls, user_name, user_id, email, password):
        Facilitator(user_name, user_id, email, password)
        cls.facilitators.append(Facilitator(user_name, user_id, email, password))


    def get_facilitator_size(cls):
        return len(cls.facilitators)

# admin = Admin("John", "123BD", "john123@gmail.com", "0000")
# admin.create_facilitator("John", "123BD", "john123@gmail.com", "0000")
#
# print(admin.get_facilitator_size())







