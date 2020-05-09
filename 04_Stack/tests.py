from Stack import Stack
from LinkedListStack import LinkedListStack
from additional_tasks import check_scopes_seq, count_postfix_expr


class TestStack:
    def test_push(self):
        stack = Stack()

        stack.push(0)
        stack.push(1)

        assert stack.peek() == 1
        assert stack.size() == 2

    def test_size(self):
        stack = Stack()
        assert stack.size() == 0

        stack.push(0)
        stack.push(1)

        assert stack.size() == 2

    def test_pop(self):
        stack = Stack()
        assert stack.pop() is None

        stack.push(0)
        stack.push(1)

        assert stack.size() == 2
        assert stack.pop() == 1
        assert stack.size() == 1

    def test_peek(self):
        stack = Stack()

        assert stack.peek() is None

        stack.push(0)
        stack.push(1)

        assert stack.peek() == 1


class TestLinkedListStack:
    def test_size(self):
        stack = LinkedListStack()
        assert stack.size() == 0

        stack.push(0)
        stack.push(1)

        assert stack.size() == 2

    def test_peek(self):
        stack = LinkedListStack()
        assert stack.peek() is None

        stack.push(0)
        stack.push(1)

        assert stack.peek() == 1

    def test_push(self):
        stack = LinkedListStack()

        stack.push(0)
        stack.push(1)

        assert stack.peek() == 1

    def test_pop(self):
        stack = LinkedListStack()
        assert stack.pop() is None

        stack.push(0)
        stack.push(1)

        assert stack.size() == 2
        assert stack.pop() == 1
        assert stack.size() == 1


class TestAdditionalTasks:
    def test_check_scopes_seq(self):
        assert check_scopes_seq('()(fghj)(') is False
        assert check_scopes_seq('()sdf(dfsg)') is True

    def test_count_postfix_expr(self):
        assert count_postfix_expr('1 2 + 3 * =') == 9
        assert count_postfix_expr('8 2 + 5 * 9 + =') == 59
