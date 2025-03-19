class MyArray:
    def __init__(self):
        self.data = [5]

    def insert(self, index, value):
        self.data.insert(index, value)

    def delete(self, index):
        if 0 <= index < len(self.data):
            self.data.pop(index)
        else:
            raise IndexError("Index out of range")

    def get(self, index):

        if 0 <= index < len(self.data):
            return self.data[index]
        else:
            raise IndexError("Index out of range")

    def size(self):

        return len(self.data)

    def __str__(self):
        return str(self.data)