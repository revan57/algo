
class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp  # used in linear probing collision resolution
        self.slots = [None] * self.size

    def hash_fun(self, value):
        return hash(value) & (self.size - 1)

    def seek_slot(self, value):
        return self.hash_fun(value) if self.size > 0 else None

    def put(self, value):
        idx = self.seek_slot(value)

        if idx is not None:
            if self.slots[idx] is None:
                self.slots[idx] = LinkedList()
                self.slots[idx].add_in_head(Node(value))
            else:
                self.slots[idx].add_in_head(Node(value))

        return idx

    def find(self, value):
        result = None
        idx = self.seek_slot(value)

        if idx is not None and self.slots[idx] is not None:
            node = self.slots[idx].head
            while node:
                if node.value == value:
                    result = idx
                    break
                node = node.next

        return result


class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_head(self, new_node):
        if self.head is None:
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node
