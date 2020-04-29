
class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


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
        while node is not None:
            if node.value == val:
                if self.head == node:
                    self.head = node.next
                    if self.head:
                        self.head.prev = None
                elif self.tail == node:
                    self.tail = node.prev
                    node.prev.next = None
                else:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                if all is False:
                    break

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
        if afterNode is None and self.head is None:
            self.add_in_head(newNode)
        elif afterNode is None and self.head:
            self.add_in_tail(newNode)
        elif afterNode == self.tail:
            self.add_in_tail(newNode)
        else:
            newNode.next = afterNode.next
            newNode.next.prev = newNode
            newNode.prev = afterNode
            afterNode.next = newNode

    def add_in_head(self, newNode):
        if self.head is None:
            self.tail = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
        self.head = newNode
