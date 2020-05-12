from HashTable import HashTable


class TestHashTable:
    def test_hash_fun(self):
        size = 7
        table = HashTable(size, 0)

        assert table.hash_fun('abc') == len('abc'.encode('utf-8')) % size
        assert table.hash_fun('абс') == len('абс'.encode('utf-8')) % size

    def test_seek_slot(self):
        size = 7
        table = HashTable(size, 0)

        assert table.seek_slot('abc') == table.hash_fun('abc')
        assert table.seek_slot('абс') == table.hash_fun('абс')

    def test_put(self):
        size = 7
        table = HashTable(size, 0)

        assert table.put('abc') == table.hash_fun('abc')
        assert table.put('абс') == table.hash_fun('абс')

    def test_find(self):
        size = 7
        table = HashTable(size, 0)

        assert table.find('abc') is None
        table.put('abc')
        assert table.find('abc') == table.hash_fun('abc')
        assert table.find('lol') is None
