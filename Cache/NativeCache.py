class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def hash_fun(self, key):
        return hash(key) & (self.size - 1)

    def is_key(self, key):
        idx = self.hash_fun(key)
        slot = self.square_probing(key, idx)
        if slot is None:
            slot = self.linear_probing(key, idx)

        return True if self.slots[slot] is not None else False

    def put(self, key, value):
        idx = self.hash_fun(key)
        slot = self.square_probing(key, idx)
        if slot is None:
            slot = self.linear_probing(key, idx)

        if slot is not None:
            self.slots[slot] = key
            self.values[slot] = value
            self.hits[slot] += 1
        else:
            slot = min(range(self.size), key=self.hits.__getitem__)
            self.hits[slot] = 1
            self.slots[slot] = key
            self.values[slot] = value

    def get(self, key):
        idx = self.hash_fun(key)
        slot = self.square_probing(key, idx)
        if slot is None:
            slot = self.linear_probing(key, idx)

        if slot is not None:
            self.hits[slot] += 1
            return self.values[slot]

        return None

    def square_probing(self, key, idx):
        i = idx
        is_arr_passed = False
        while True:
            if i >= self.size:
                i = 0
                is_arr_passed = True

            if self.slots[i] == key or self.slots[i] is None:
                return i

            if i >= idx and is_arr_passed:
                return None

            if i == 0 or i == 1:
                i = i + 1
            else:
                i = i ** 2

    def linear_probing(self, key, idx):
        i = idx
        is_arr_passed = False
        while True:
            if i >= self.size:
                i = 0
                is_arr_passed = True

            if self.slots[i] == key or self.slots[i] is None:
                return i

            if i >= idx and is_arr_passed:
                return None

            i = i + 1
