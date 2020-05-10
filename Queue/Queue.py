
class Queue:
    def __init__(self):
        self.queue = LinkedList2()

    def enqueue(self, item):
        self.queue.add_in_tail(Node(item))

    def dequeue(self):
        return self.queue.pop_from_head()

    def size(self):
        return self.queue.len()


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

    def len(self):
        node = self.head
        length = 0

        while node is not None:
            length += 1
            node = node.next

        return length


class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None
