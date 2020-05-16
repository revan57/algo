from Set import PowerSet


class TestSet:
    def test_put(self):
        set = PowerSet()
        assert set.size() == 0
        set.put('test_1')
        set.put('test')
        set.put('test')

        assert set.size() == 2
        assert set.get('test_1') is True
        assert set.get('test') is True
        assert len(set.get_all_values()) == 2

    def test_get(self):
        set = PowerSet()
        set.put('lol')
        set.put('test')

        assert set.get('lol') is True
        assert set.get('test') is True
        assert set.get('lal') is False

    def test_remove(self):
        set = PowerSet()
        set.put('lol')
        set.put('test')

        assert set.size() == 2

        assert set.remove('lol')
        assert set.size() == 1
        assert set.get('lol') is False
        assert set.get_all_values()[0] == 'test'

        assert set.remove('test_2') is False

        assert set.remove('test')
        assert set.size() == 0
        assert len(set.get_all_values()) == 0
        assert set.get('test') is False

    def test_intersection(self):
        set_1 = PowerSet()
        set_1.put('test_1')
        set_1.put('test_2')
        set_1.put('test_3')

        set_2 = PowerSet()
        set_2.put('test_55')

        res = set_1.intersection(set_2)
        assert len(res.get_all_values()) == 0
        assert res.size() == 0

        set_2.put('test_2')
        set_2.put('test_3')
        set_2.put('test_4')

        res = set_1.intersection(set_2)
        assert res.size() == 2
        assert len(res.get_all_values()) == 2
        assert 'test_2' in res.get_all_values()
        assert 'test_3' in res.get_all_values()

    def test_union(self):
        set_1 = PowerSet()
        set_1.put('test_1')
        set_1.put('test_2')
        set_1.put('test_3')

        set_2 = PowerSet()

        res = set_1.union(set_2)
        assert res.size() == 3
        assert len(res.get_all_values()) == 3
        assert 'test_1' in res.get_all_values()
        assert 'test_2' in res.get_all_values()
        assert 'test_3' in res.get_all_values()

        set_2.put('test_2')
        set_2.put('test_3')
        set_2.put('test_4')

        res = set_1.union(set_2)
        assert res.size() == 4
        assert len(res.get_all_values()) == 4
        assert 'test_1' in res.get_all_values()
        assert 'test_2' in res.get_all_values()
        assert 'test_3' in res.get_all_values()
        assert 'test_4' in res.get_all_values()

    def test_difference(self):
        set_1 = PowerSet()
        set_1.put('test_1')
        set_1.put('test_2')
        set_1.put('test_3')

        set_2 = PowerSet()
        set_2.put('test_1')
        set_2.put('test_2')
        set_2.put('test_3')

        res = set_1.difference(set_2)
        assert res.size() == 0
        assert len(res.get_all_values()) == 0

        set_1.put('test_4')
        set_1.put('test_5')

        res = set_1.difference(set_2)
        assert res.size() == 2
        assert len(res.get_all_values()) == 2
        assert 'test_4' in res.get_all_values()
        assert 'test_5' in res.get_all_values()

    def test_issubset(self):
        set_1 = PowerSet()
        set_1.put('test_1')
        set_1.put('test_2')
        set_1.put('test_3')

        set_2 = PowerSet()
        assert set_1.issubset(set_2) is True

        set_2.put('test_1')
        set_2.put('test_2')
        assert set_1.issubset(set_2) is True

        set_2.put('test_3')
        assert set_1.issubset(set_2) is True

        set_2.put('test_4')
        assert set_1.issubset(set_2) is False
