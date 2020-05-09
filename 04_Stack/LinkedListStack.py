
class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedListStack:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, val):
        new_node = Node(val)

        if self.head is None:
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node

    def pop(self):
        val = None

        if self.head:
            val = self.head.value
            self.head = self.head.next
            if self.head:
                self.head.prev = None

        if self.head is None:
            self.tail = None

        return val

    def peek(self):
        return self.head.value if self.head else None

    def size(self):
        node = self.head
        length = 0

        while node is not None:
            length += 1
            node = node.next

        return length
