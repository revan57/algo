from LinkedList import LinkedList, Node


def test_clean():
    linked_list = LinkedList()
    linked_list.add_in_tail(Node(1))
    linked_list.add_in_tail(Node(2))
    linked_list.add_in_tail(Node(3))
    linked_list.add_in_tail(Node(4))

    linked_list.clean()

    assert linked_list.head is None
    assert linked_list.tail is None


def test_length():
    list_length = 4
    linked_list = LinkedList()

    assert linked_list.len() == 0

    for i in range(list_length):
        linked_list.add_in_tail(Node(1))

    assert linked_list.len() == list_length


def test_insert_after_node():
    linked_list = LinkedList()
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
    assert n4.next == n2

    # inserting into tail:
    linked_list.insert(n3, n5)

    assert n3.next == n5
    assert n5.next is None
    assert linked_list.tail == n5


def test_deleting_single_value():
    linked_list = LinkedList()

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
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(3)
    linked_list.add_in_tail(n1)
    linked_list.add_in_tail(n2)
    linked_list.add_in_tail(n3)
    linked_list.add_in_tail(n4)

    linked_list.delete(3)
    assert linked_list.head == n1
    assert linked_list.tail == n4
    assert linked_list.len() == 3


def test_deleting_all_values():
    linked_list = LinkedList()

    linked_list.delete(0, True)
    assert linked_list.head is None
    assert linked_list.tail is None

    # single-element list
    linked_list.add_in_tail(Node(1))

    assert linked_list.len() == 1

    linked_list.delete(1, True)
    assert linked_list.len() == 0
    assert linked_list.head is None
    assert linked_list.tail is None

    # multi-element list
    n1 = Node(1)
    n2 = Node(1)
    n3 = Node(2)
    n4 = Node(3)
    n5 = Node(4)
    n6 = Node(5)
    n7 = Node(5)
    linked_list.add_in_tail(n1)
    linked_list.add_in_tail(n2)
    linked_list.add_in_tail(n3)
    linked_list.add_in_tail(n4)
    linked_list.add_in_tail(n5)
    linked_list.add_in_tail(n6)
    linked_list.add_in_tail(n7)

    assert linked_list.len() == 7

    # deleting from middle
    linked_list.delete(4, True)
    assert linked_list.head == n1
    assert linked_list.tail == n7
    assert linked_list.len() == 6

    # deleting from tail
    linked_list.delete(5, True)
    assert linked_list.head == n1
    assert linked_list.tail == n4
    assert linked_list.len() == 4

    # deleting from head
    linked_list.delete(1, True)
    assert linked_list.head == n3
    assert linked_list.tail == n4
    assert linked_list.len() == 2


def test_find_all_values():
    linked_list = LinkedList()
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


# 1.1
test_deleting_single_value()
# 1.2
test_deleting_all_values()
# 1.3
test_clean()
# 1.4
test_find_all_values()
# 1.5
test_length()
# 1.6
test_insert_after_node()
