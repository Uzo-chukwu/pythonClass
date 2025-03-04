class User:
    def __init__(self, user_name, user_id, email, password):
        self.__user_name = user_name
        self.__user_id = user_id
        self.__email = email
        self.__password = password

    @property
    def get_user_name(self):
        return self.__user_name

    @property
    def get_user_id(self):
        return self.__user_id

    @property
    def get_email(self):
        return self.__email

    @property
    def validate_password(self, password):
        return password == self.__password