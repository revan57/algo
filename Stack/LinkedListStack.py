from LinkedList2.LinkedList2 import LinkedList2, Node


class LinkedListStack:
    def __init__(self):
        self.stack = LinkedList2()

    def push(self, val):
        self.stack.add_in_head(Node(val))

    def pop(self):
        return self.stack.delete_from_head()

    def peek(self):
        return self.stack.head.value if self.stack.head else None

    def size(self):
        return self.stack.len()
