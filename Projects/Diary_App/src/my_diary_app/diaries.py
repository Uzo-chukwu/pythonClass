from diary import Diary


class Diaries:
    def __init__(self):
        self.diaries = []

    def create_diary(self, username, password):
        if not username.strip() or not password.strip():
            raise ValueError("Username or Password cannot be empty")
        self.diaries.append(Diary(username, password))

    def find_diary_by_username(self, username, password):
        for diary in self.diaries:
            if diary.get_username() == username and diary.validate_password(password):
                return diary
        raise ValueError("Wrong Username or Password")

    def remove_diary(self, username, password):
        diary = self.find_diary_by_username(username, password)
        self.diaries.remove(diary)