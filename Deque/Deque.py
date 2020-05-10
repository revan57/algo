class Deque:
    def __init__(self):
        self.deque = LinkedList2()

    def addFront(self, item):
        self.deque.add_in_head(Node(item))

    def addTail(self, item):
        self.deque.add_in_tail(Node(item))

    def removeFront(self):
        return self.deque.pop_from_head()

    def removeTail(self):
        return self.deque.pop_from_tail()

    def size(self):
        return self.deque.len()


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def add_in_head(self, new_node):
        if self.head is None:
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node

    def pop_from_head(self):
        val = None

        if self.head:
            val = self.head.value
            self.head = self.head.next
            if self.head:
                self.head.prev = None

        if self.head is None:
            self.tail = None

        return val

    def pop_from_tail(self):
        val = None

        if self.tail:
            val = self.tail.value
            if self.tail.prev:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                self.tail = None
                self.head = None

        return val

    def len(self):
        node = self.head
        length = 0

        while node is not None:
            length += 1
            node = node.next

        return length

    def print_all_nodes(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next


class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None
