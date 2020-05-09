class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        return self.stack.pop() if self.size() > 0 else None

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        return self.stack[-1] if self.size() > 0 else None
