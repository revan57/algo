import random
import string

from SetLinearResolve import PowerSet as LinearPowerSet
from SetChainResolve import PowerSet as ChainPowerSet


class TestSetLinearResolve:
    def test_put(self):
        set = LinearPowerSet()
        assert set.size() == 0
        set.put('test_1')
        set.put('test')
        set.put('test')

        assert set.size() == 2
        assert set.get('test_1') is True
        assert set.get('test') is True
        assert len(set.get_all_values()) == 2

    def test_get(self):
        set = LinearPowerSet()
        set.put('lol')
        set.put('test')

        assert set.get('lol') is True
        assert set.get('test') is True
        assert set.get('lal') is False

    def test_remove(self):
        # TODO correct remove
        """
        set_1 = LinearPowerSet()
        letters = string.ascii_letters

        values = {''.join(random.choice(letters) for i in range(16)) for j in range(20000)}

        for value in values:
            set_1.put(value)

        assert len(set_1.get_all_values()) == len(values)
        assert set_1.size() == len(values)

        for value in values:
            try:
                assert set_1.remove(value)
            except Exception:
                raise Exception(value, set_1.get(value), value in set_1.slots)

        assert set_1.size() == 0
        assert len(set_1.get_all_values()) == 0
        """
        pass

    def test_intersection(self):
        set_1 = LinearPowerSet()
        set_1.put('test_1')
        set_1.put('test_2')
        set_1.put('test_3')

        set_2 = LinearPowerSet()
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
        set_1 = LinearPowerSet()
        set_1.put('test_1')
        set_1.put('test_2')
        set_1.put('test_3')

        set_2 = LinearPowerSet()

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
        set_1 = LinearPowerSet()
        set_1.put('test_1')
        set_1.put('test_2')
        set_1.put('test_3')

        set_2 = LinearPowerSet()
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
        set_1 = LinearPowerSet()
        set_1.put('test_1')
        set_1.put('test_2')
        set_1.put('test_3')

        set_2 = LinearPowerSet()
        assert set_1.issubset(set_2) is True

        set_2.put('test_1')
        set_2.put('test_2')
        assert set_1.issubset(set_2) is True

        set_2.put('test_3')
        assert set_1.issubset(set_2) is True

        set_2.put('test_4')
        assert set_1.issubset(set_2) is False


class TestChainSet:
    def test_put(self):
        set = ChainPowerSet()
        assert set.size() == 0
        set.put('test_1')
        set.put('test')
        set.put('test')

        assert set.size() == 2
        assert set.get('test_1') is True
        assert set.get('test') is True
        assert len(set.get_all_values()) == 2

    def test_get(self):
        set = ChainPowerSet()
        set.put('lol')
        set.put('test')

        assert set.get('lol') is True
        assert set.get('test') is True
        assert set.get('lal') is False

    def test_remove(self):
        set_1 = ChainPowerSet()
        letters = string.ascii_letters

        values = {''.join(random.choice(letters) for i in range(16)) for j in range(20000)}

        for value in values:
            set_1.put(value)

        assert len(set_1.get_all_values()) == len(values)
        assert set_1.size() == len(values)

        for value in values:
            assert set_1.remove(value)

        assert set_1.size() == 0
        assert len(set_1.get_all_values()) == 0

    def test_intersection(self):
        set_1 = ChainPowerSet()
        set_1.put('test_1')
        set_1.put('test_2')
        set_1.put('test_3')

        set_2 = ChainPowerSet()
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
        set_1 = ChainPowerSet()
        set_1.put('test_1')
        set_1.put('test_2')
        set_1.put('test_3')

        set_2 = ChainPowerSet()

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
        set_1 = ChainPowerSet()
        set_1.put('test_1')
        set_1.put('test_2')
        set_1.put('test_3')

        set_2 = ChainPowerSet()
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
        set_1 = ChainPowerSet()
        set_1.put('test_1')
        set_1.put('test_2')
        set_1.put('test_3')

        set_2 = ChainPowerSet()
        assert set_1.issubset(set_2) is True

        set_2.put('test_1')
        set_2.put('test_2')
        assert set_1.issubset(set_2) is True

        set_2.put('test_3')
        assert set_1.issubset(set_2) is True

        set_2.put('test_4')
        assert set_1.issubset(set_2) is False
