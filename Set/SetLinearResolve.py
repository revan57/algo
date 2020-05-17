class HashTable:
    def __init__(self, sz):
        # should be a power of 2
        self.t_size = sz
        # https://github.com/python/cpython/blob/master/Objects/dictobject.c#L133
        self.PERTURB_SHIFT = 5
        self.MASK = self.t_size - 1
        self.slots = [None] * self.t_size

    # https://github.com/python/cpython/blob/master/Objects/dictobject.c#L1162
    def hash_fun(self, key):
        return hash(key) & self.MASK

    def is_key(self, key):
        ix = self.find_empty_slot(key)
        return True if self.slots[ix] is not None else False

    def put(self, key):
        ix = self.find_empty_slot(key)
        self.slots[ix] = key

    def get(self, key):
        idx = self.find_empty_slot(key)

        if idx is not None:
            return True

        return False

    # https://github.com/python/cpython/blob/master/Objects/dictobject.c#L1028
    def find_empty_slot(self, key):
        i = self.hash_fun(key)
        ix = self.dictkeys_get_index(key, i)
        perturb = hash(key)
        while ix < 0:
            perturb = perturb >> self.PERTURB_SHIFT
            i = (i * 5 + perturb + 1) & self.MASK
            ix = self.dictkeys_get_index(key, i)

        return ix

    def dictkeys_get_index(self, key, i):
        if self.slots[i] == key:
            return i
        elif self.slots[i] is None:
            return i
        return -1


class PowerSet(HashTable):
    def __init__(self):
        super().__init__(32768)
        self.fill_size = 0

    def size(self):
        return self.fill_size

    def put(self, value):
        idx = self.find_empty_slot(value)

        if idx is not None:
            if self.slots[idx] != value:
                self.slots[idx] = value
                self.fill_size += 1

    def get(self, value):
        idx = self.find_empty_slot(value)
        if idx is not None and self.slots[idx] == value:
            return True

        return False

    def remove(self, value):
        idx = self.find_empty_slot(value)
        if idx is not None and self.slots[idx] == value:
            self.slots[idx] = None
            self.fill_size -= 1
            return True

        return False

    def intersection(self, set2):
        result_set = PowerSet()
        for value in self.slots:
            if value is not None:
                if set2.get(value):
                    result_set.put(value)

        return result_set

    def union(self, set2):
        result_set = PowerSet()
        result_set.slots = self.slots.copy()
        result_set.fill_size = self.fill_size

        for value in set2.slots:
            if value is not None:
                result_set.put(value)

        return result_set

    def difference(self, set2):
        result_set = PowerSet()
        for value in self.slots:
            if value is not None:
                if not set2.get(value):
                    result_set.put(value)

        return result_set

    def issubset(self, set2):
        for value in set2.slots:
            if value is not None:
                if not self.get(value):
                    return False

        return True

    def get_all_values(self):
        elems = []
        for value in self.slots:
            if value is not None:
                elems.append(value)

        return elems
