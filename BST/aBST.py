class aBST:

    def __init__(self, depth):
        tree_size = 2 ** (depth + 1) - 1
        self.Tree = [None] * tree_size  # keys arr

    def FindKeyIndex(self, key):
        i = 0
        while True:
            if i >= len(self.Tree):
                break
            if self.Tree[i] is None:
                return -i if i > 0 else 0
            if self.Tree[i] == key:
                return i

            if key > self.Tree[i]:
                i = int(2 * i + 2)
            elif key < self.Tree[i]:
                i = int(2 * i + 1)

        return None

    def AddKey(self, key):
        res_idx = self.FindKeyIndex(key)

        if res_idx is None:
            return -1
        if res_idx > 0:
            return res_idx
        if res_idx < 0:
            self.Tree[abs(res_idx)] = key
            return abs(res_idx)
        if res_idx == 0:
            if self.Tree[0] is None:
                self.Tree[0] = key
                return 0
            else:
                return 0
