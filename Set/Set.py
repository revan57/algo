from HashTable import HashTable, LinkedList, Node


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
