from datetime import datetime

class Entry:
    def __init__(self, title, body, id):
        self.title = title
        self.body = body
        self.id = id
        self.date_created = datetime.now().replace(second=0, microsecond=0)

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_body(self):
        return self.body

    def set_body(self, body):
        self.body = body

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_date_created(self):
        return self.date_created

    def __str__(self):
        return f"{self.title}\n{self.body}\nTime created: {self.date_created}"