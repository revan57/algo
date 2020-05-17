class HashTable:
    def __init__(self, sz):
        self.t_size = sz
        self.slots = [None] * self.t_size
        self.MASK = self.t_size - 1

    def hash_fun(self, value):
        return hash(value) & self.MASK

    def seek_slot(self, value):
        return self.hash_fun(value) if self.t_size > 0 else None

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

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next

        return None

    def delete(self, val):
        is_deleted = False
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

                is_deleted = True
                break

            node = node.next

        if self.head is None:
            self.tail = None

        return is_deleted


class PowerSet(HashTable):
    def __init__(self):
        super().__init__(20000)
        self.fill_size = 0

    def size(self):
        return self.fill_size

    def put(self, value):
        idx = self.seek_slot(value)

        if idx is not None:
            if self.slots[idx] is None:
                self.slots[idx] = LinkedList()
                self.slots[idx].add_in_head(Node(value))
                self.fill_size += 1
            else:
                if self.slots[idx].find(value) is None:
                    self.slots[idx].add_in_head(Node(value))
                    self.fill_size += 1

        return idx

    def get(self, value):
        idx = self.seek_slot(value)
        if idx is not None and self.slots[idx] is not None:
            node = self.slots[idx].head
            while node:
                if node.value == value:
                    return True

                node = node.next

        return False

    def remove(self, value):
        idx = self.seek_slot(value)
        if idx is not None and self.slots[idx] is not None:
            is_deleted = self.slots[idx].delete(value)

            if is_deleted:
                self.fill_size -= 1
                return True

        return False

    def intersection(self, set2):
        result_set = PowerSet()
        for el in self.slots:
            if el is not None:
                node = el.head
                while node:
                    if set2.get(node.value):
                        result_set.put(node.value)
                    node = node.next

        return result_set

    def union(self, set2):
        result_set = PowerSet()
        result_set.slots = self.slots.copy()
        result_set.fill_size = self.fill_size

        for el in set2.slots:
            if el is not None:
                node = el.head
                while node:
                    result_set.put(node.value)
                    node = node.next

        return result_set

    def difference(self, set2):
        result_set = PowerSet()
        for el in self.slots:
            if el is not None:
                node = el.head
                while node:
                    if not set2.get(node.value):
                        result_set.put(node.value)
                    node = node.next

        return result_set

    def issubset(self, set2):
        for el in set2.slots:
            if el is not None:
                node = el.head
                while node:
                    if not self.get(node.value):
                        return False
                    node = node.next
        return True

    def get_all_values(self):
        elems = []
        for el in self.slots:
            if el is not None:
                node = el.head
                while node:
                    elems.append(node.value)
                    node = node.next

        return elems
