from OrderedList import OrderedList, OrderedStringList


class TestOrderedList:
    def test_compare(self):
        ol = OrderedList(True)
        assert ol.compare(0, 1) == -1
        assert ol.compare(1, 0) == 1
        assert ol.compare(1, 1) == 0

    def test_add_ascending(self):
        ol = OrderedList(True)
        ol.add(-1)
        ol.add(-1)
        ol.add(13)
        ol.add(15)
        ol.add(-16)

        ol_elements = ol.get_all()
        assert ol_elements[0] == -16
        assert ol_elements[1] == -1
        assert ol_elements[2] == -1
        assert ol_elements[3] == 13
        assert ol_elements[4] == 15
        assert ol.len() == 5

    def test_add_descending(self):
        ol = OrderedList(False)
        ol.add(-1)
        ol.add(-1)
        ol.add(13)
        ol.add(15)
        ol.add(-16)

        ol_elements = ol.get_all()
        assert ol_elements[0] == 15
        assert ol_elements[1] == 13
        assert ol_elements[2] == -1
        assert ol_elements[3] == -1
        assert ol_elements[4] == -16
        assert ol.len() == 5

    def test_find_elem(self):
        ol = OrderedList(True)
        ol.add(0)
        ol.add(1)
        ol.add(2)

        assert ol.find(3) is None
        assert ol.find(2).value == 2

    def test_delete_elem(self):
        ol = OrderedList(True)
        ol.add(0)
        ol.add(1)
        ol.add(2)

        ol.delete(2)
        assert ol.len() == 2

        ol_elements = ol.get_all()
        assert 2 not in ol_elements


class TestOrderedStringList:
    def test_compare(self):
        osl = OrderedStringList(True)
        assert osl.compare('  a', 'b') == -1
        assert osl.compare('z', '   v   ') == 1
        assert osl.compare('   aaa   ', '   aaa   ') == 0
