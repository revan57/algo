from LinkedList import LinkedList, Node


def lists_sum(list_1, list_2):
    if isinstance(list_1, LinkedList) and isinstance(list_2, LinkedList):
        if list_1.len() == list_2.len():
            result_list = LinkedList()

            node_1 = list_1.head
            node_2 = list_2.head
            while node_1 is not None:
                if not isinstance(node_1.value, int) or not isinstance(node_2.value, int):
                    raise TypeError('Lists values should be integers.')
                result_list.add_in_tail(Node(node_1.value + node_2.value))

                node_1 = node_1.next
                node_2 = node_2.next

            return result_list
        else:
            raise Exception('Lists has different length.')
    else:
        raise TypeError('Argument should be an instance of LinkedList.')
