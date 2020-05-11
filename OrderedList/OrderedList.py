class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        elif v1 > v2:
            return 1
        return 0

    def __add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def add_in_head(self, new_node):
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def __insert(self, after_node, new_node):
        new_node.next = after_node.next
        new_node.next.prev = new_node
        new_node.prev = after_node
        after_node.next = new_node

    def add(self, value):
        if self.head is None:
            self.__add_in_tail(Node(value))
        else:
            node = self.head
            while node is not None:
                if node == self.tail:
                    cur_node_compare = self.compare(value, node.value)
                    if self.__ascending:
                        if cur_node_compare == 1 or cur_node_compare == 0:
                            self.__add_in_tail(Node(value))
                        else:
                            self.add_in_head(Node(value))
                    else:
                        if cur_node_compare == -1 or cur_node_compare == 0:
                            self.__add_in_tail(Node(value))
                        else:
                            self.add_in_head(Node(value))
                    break
                else:
                    cur_node_compare = self.compare(value, node.value)
                    next_node_compare = self.compare(value, node.next.value)

                    if self.__ascending:
                        if (cur_node_compare == 1 and next_node_compare == -1) or cur_node_compare == 0 or next_node_compare == 0:
                            self.__insert(node, Node(value))
                            break
                    else:
                        if (cur_node_compare == -1 and next_node_compare == 1) or cur_node_compare == 0 or next_node_compare == 0:
                            self.__insert(node, Node(value))
                            break
                node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if self.__ascending:
                if node.value > val:
                    break
            else:
                if node.value < val:
                    break
            if node.value == val:
                return node
            node = node.next
        return None

    def delete(self, val):
        node = self.head
        while node is not None:
            if self.__ascending:
                if node.value > val:
                    break
            else:
                if node.value < val:
                    break
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
                
                break

            node = node.next

        if self.head is None:
            self.tail = None

    def clean(self, asc):
        self.__ascending = asc
        self.head = None
        self.tail = None

    def len(self):
        counter = 0
        node = self.head
        while node:
            counter += 1
            node = node.next

        return counter

    def get_all(self):
        r = []
        node = self.head
        while node:
            r.append(node.value)
            node = node.next
        return r


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        v1 = v1.strip()
        v2 = v2.strip()

        if v1 < v2:
            return -1
        elif v1 > v2:
            return 1

        return 0
