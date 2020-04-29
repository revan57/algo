from LinkedList2 import LinkedList2, Node


class TestClass:
    def test_clean(self):
        linked_list = LinkedList2()
        linked_list.add_in_tail(Node(1))
        linked_list.add_in_tail(Node(2))
        linked_list.add_in_tail(Node(3))
        linked_list.add_in_tail(Node(4))

        linked_list.clean()

        assert linked_list.head is None
        assert linked_list.tail is None

    def test_length(self):
        list_length = 4
        linked_list = LinkedList2()

        assert linked_list.len() == 0

        for i in range(list_length):
            linked_list.add_in_tail(Node(1))

        assert linked_list.len() == list_length

    def test_insert_after_node(self):
        linked_list = LinkedList2()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)
        n5 = Node(5)

        # inserting into empty list
        linked_list.insert(None, n1)
        assert linked_list.head == n1
        assert linked_list.tail == n1

        linked_list.add_in_tail(n2)
        linked_list.add_in_tail(n3)

        # inserting into list middle
        linked_list.insert(n1, n4)

        assert n1.next == n4
        assert n2.prev == n4
        assert n4.prev == n1
        assert n4.next == n2

        # inserting into tail:
        linked_list.insert(n3, n5)

        assert n3.next == n5
        assert n5.next is None
        assert n5.prev == n3
        assert linked_list.tail == n5

    def test_find_value(self):
        linked_list = LinkedList2()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(2)

        assert linked_list.find(1) is None

        linked_list.add_in_tail(n1)
        linked_list.add_in_tail(n2)
        linked_list.add_in_tail(n3)

        assert linked_list.find(1) == n1

    def test_find_all_values(self):
        linked_list = LinkedList2()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(2)

        assert len(linked_list.find_all(1)) == 0

        linked_list.add_in_tail(n1)
        linked_list.add_in_tail(n2)
        linked_list.add_in_tail(n3)

        # find uniq value
        search_result = linked_list.find_all(1)
        assert len(search_result) == 1 and search_result[0] == n1

        # find repeating values
        search_result = linked_list.find_all(2)
        assert len(search_result) == 2 and search_result[0] == n2 and search_result[1] == n3

    def test_add_in_head(self):
        linked_list = LinkedList2()
        n1 = Node(1)
        n2 = Node(2)

        # add in empty list
        linked_list.add_in_head(n1)

        assert linked_list.head == n1
        assert linked_list.tail == n1

        # add in non empty list
        linked_list.add_in_head(n2)

        assert linked_list.head == n2
        assert linked_list.tail == n1
        assert n1.next is None
        assert n2.prev is None
        assert n1.prev is n2
        assert n2.next is n1

    def test_deleting_single_value(self):
        linked_list = LinkedList2()

        linked_list.delete(0)
        assert linked_list.head is None
        assert linked_list.tail is None

        # single-element list
        linked_list.add_in_tail(Node(1))

        linked_list.delete(1)
        assert linked_list.len() == 0
        assert linked_list.head is None
        assert linked_list.tail is None

        # multi-element list
        n1 = Node(1)
        n2 = Node(1)
        n3 = Node(2)
        n4 = Node(3)
        n5 = Node(4)
        linked_list.add_in_tail(n1)
        linked_list.add_in_tail(n2)
        linked_list.add_in_tail(n3)
        linked_list.add_in_tail(n4)
        linked_list.add_in_tail(n5)

        # deleting head value
        linked_list.delete(1)
        assert linked_list.head == n2
        assert n2.prev is None
        assert n2.next == n3
        assert n3.prev == n2
        assert linked_list.tail == n5
        assert linked_list.len() == 4

        # deleting tail value
        linked_list.delete(4)
        assert linked_list.head == n2
        assert linked_list.tail == n4
        assert n4.next is None
        assert n4.prev == n3
        assert linked_list.len() == 3

        # deleting middle value
        linked_list.delete(2)
        assert linked_list.head == n2
        assert linked_list.tail == n4
        assert n2.next == n4
        assert n4.prev == n2
        assert linked_list.len() == 2

    def test_deleting_all_values(self):
        linked_list = LinkedList2()

        linked_list.delete(0, True)
        assert linked_list.head is None
        assert linked_list.tail is None

        # single-element list
        linked_list.add_in_tail(Node(1))

        linked_list.delete(1, True)
        assert linked_list.len() == 0
        assert linked_list.head is None
        assert linked_list.tail is None

        # multi-element list
        n1 = Node(1)
        n2 = Node(1)
        n3 = Node(2)
        n4 = Node(3)
        n5 = Node(3)
        n6 = Node(4)
        n7 = Node(5)
        n8 = Node(5)
        linked_list.add_in_tail(n1)
        linked_list.add_in_tail(n2)
        linked_list.add_in_tail(n3)
        linked_list.add_in_tail(n4)
        linked_list.add_in_tail(n5)
        linked_list.add_in_tail(n6)
        linked_list.add_in_tail(n7)
        linked_list.add_in_tail(n8)

        # deleting head value
        linked_list.delete(1, True)
        assert linked_list.head == n3
        assert n3.prev is None
        assert n3.next == n4
        assert n4.prev == n3
        assert linked_list.tail == n8
        assert linked_list.len() == 6

        # deleting tail value
        linked_list.delete(5, True)
        assert linked_list.head == n3
        assert linked_list.tail == n6
        assert n6.next is None
        assert n6.prev == n5
        assert linked_list.len() == 4

        # deleting middle value
        linked_list.delete(3, True)
        assert linked_list.head == n3
        assert linked_list.tail == n6
        assert n3.next == n6
        assert n6.prev == n3
        assert linked_list.len() == 2

        # test deleting in list with equal value
        linked_list = LinkedList2()
        linked_list.add_in_tail(Node(1))
        linked_list.add_in_tail(Node(1))
        linked_list.add_in_tail(Node(1))

        linked_list.delete(1, True)

        assert linked_list.len() == 0
        assert linked_list.head is None
        assert linked_list.tail is None
