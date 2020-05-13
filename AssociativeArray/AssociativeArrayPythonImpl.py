class NativeDictionary:
    def __init__(self, sz):
        # should be a power of 2
        self.size = sz
        # https://github.com/python/cpython/blob/master/Objects/dictobject.c#L133
        self.PERTURB_SHIFT = 5
        self.MASK = self.size - 1
        self.slots = [None] * self.size
        self.values = [None] * self.size

        if not self.is_power_of_two(self.size):
            raise Exception('Dict size should be a power of 2')

    # https://github.com/python/cpython/blob/master/Objects/dictobject.c#L1162
    def hash_fun(self, key):
        return hash(key) & self.MASK

    def is_key(self, key):
        ix = self.find_empty_slot(key)
        return True if self.slots[ix] is not None else False

    def put(self, key, value):
        ix = self.find_empty_slot(key)
        self.slots[ix] = key
        self.values[ix] = value

    def get(self, key):
        result = None
        idx = self.find_empty_slot(key)

        if idx is not None:
            result = self.values[idx]

        return result

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

    def is_power_of_two(self, v):
        return v & (v - 1) == 0
