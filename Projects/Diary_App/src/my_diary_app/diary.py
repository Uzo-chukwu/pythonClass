from entry import Entry


class Diary:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.is_locked = False
        self.entry_count = 1
        self.entries = []

    def get_username(self):
        return self.username

    def get_entry_count(self):
        return self.entry_count

    def validate_password(self, password):
        return self.password == password

    def is_empty(self):
        return len(self.entries) == 0

    def create_entry(self, title, body):
        if not title.strip() or not body.strip():
            raise ValueError("Field cannot be empty")
        entry = Entry(title, body, self.entry_count)
        self.entries.append(entry)
        self.entry_count += 1

    def find_entry_by_id(self, id):
        for entry in self.entries:
            if entry.get_id() == id:
                return str(entry)
        raise ValueError("Entry not found")

    def delete_entry(self, id):
        self.entries = [entry for entry in self.entries if entry.get_id() != id]

    def count_entries(self):
        return len(self.entries)

    def lock_diary(self):
        self.is_locked = True

    def unlock_diary(self):
        self.is_locked = False

    def get_is_locked(self):
        return self.is_locked

    def update_entry(self, id, title, body):
        for entry in self.entries:
            if entry.get_id() == id:
                entry.set_title(title)
                entry.set_body(body)
                return
        raise ValueError("Entry not found")