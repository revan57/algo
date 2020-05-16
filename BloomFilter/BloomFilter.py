class BloomFilter:
    def __init__(self, f_len=32):
        self.filter_len = f_len
        self.bitarray = 1 << self.filter_len

    def hash1(self, str1):
        seed = 17
        idx = 0
        for c in str1:
            idx = (idx * seed + ord(c)) % self.filter_len

        return idx

    def hash2(self, str1):
        seed = 223
        idx = 0
        for c in str1:
            idx = (idx * seed + ord(c)) % self.filter_len

        return idx

    def add(self, str1):
        positions = self.hash1(str1), self.hash2(str1),
        print(positions)
        for pos in positions:
            self.bitarray = self.bitarray | 1 << pos

    def is_value(self, str1):
        positions = self.hash1(str1), self.hash2(str1),
        print(positions)
        for pos in positions:
            if self.bitarray & 1 << pos == 0:
                return False

        return True
