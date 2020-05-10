
class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        nodes = []
        node = self.head

        while node is not None:
            if node.value == val:
                nodes.append(node)
            node = node.next

        return nodes

    def delete(self, val, all=False):
        node = self.head
        prev = self.head

        while node is not None:
            if node.value == val:
                if self.head.value == val:
                    self.head = node.next

                prev.next = node.next
                if not all:
                    if self.head is None:
                        self.tail = None
                    return
            else:
                prev = node
                self.tail = prev if all else self.tail

            node = node.next

        if self.head is None:
            self.tail = None

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        node = self.head
        length = 0

        while node is not None:
            length += 1
            node = node.next

        return length

    def insert(self, afterNode, newNode):
        if afterNode is None:
            self.head = newNode
            self.tail = newNode
        elif afterNode == self.tail:
            self.add_in_tail(newNode)
        else:
            tmp = afterNode.next
            afterNode.next = newNode
            newNode.next = tmp
