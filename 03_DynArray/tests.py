from DynArray import DynArray
import pytest


class TestClass:
    def test_insert(self):
        arr = DynArray()
        arr.insert(0, 0)
        arr.insert(0, 1)
        arr.insert(0, 2)
        arr.insert(0, 3)

        assert arr[0] == 3
        assert arr[1] == 2
        assert arr[2] == 1
        assert arr[3] == 0
        assert arr.capacity == 16

        for el in range(16):
            arr.insert(0, el)

        assert arr.count == 20
        assert arr.capacity == 32

        with pytest.raises(Exception) as e:
            assert arr.insert(100, 1)
        assert str(e.value) == 'Index is out of bounds'

    def test_delete(self):
        arr = DynArray()
        arr_len = 60
        for el in range(arr_len):
            arr.append(el)

        arr.delete(0)
        assert arr.count == 59
        assert arr[0] == 1

        prev_capacity = arr.capacity

        for el in range(int(arr_len/2 + 5)):
            arr.delete(0)

        assert arr.count == 24
        assert arr.capacity == int(prev_capacity/1.5)

        with pytest.raises(Exception) as e:
            arr.delete(100)
        assert str(e.value) == 'Index is out of bounds'
