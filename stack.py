class Stack:
    def __init__(self):
        self.storage = []

    def is_empty(self):
        return not self.storage

    def push(self, e):
        self.storage.append(e)

    def pop(self):
        if not self.is_empty():
            return self.storage.pop()
        return None

    def top(self):
        if not self.is_empty():
            return self.storage[len(self.storage)-1]
        return None

    def size(self):
        return len(self.storage)

    def __str__ (self):
        return str(self.storage)
