from Queue import Queue
from rotate_queue import rotate_queue


class TestQueue:
    def test_enqueue(self):
        queue = Queue()

        queue.enqueue(0)
        queue.enqueue(1)

        assert queue.size() == 2

    def test_dequeue(self):
        queue = Queue()

        assert queue.dequeue() is None

        queue.enqueue(0)
        queue.enqueue(1)

        assert queue.dequeue() == 0
        assert queue.dequeue() == 1
        assert queue.dequeue() is None

    def test_size(self):
        queue = Queue()
        assert queue.size() == 0

        queue.enqueue(0)
        queue.enqueue(1)

        assert queue.size() == 2


class TestAdditional:
    def test_rotate_queue(self):
        queue_elems = ''

        queue = Queue()

        queue.enqueue(0)
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        for i in range(queue.size()):
            queue_elems += str(queue.dequeue())

        assert queue_elems == '0123'
        queue_elems = ''

        queue.enqueue(0)
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        rotate_queue(queue, 3)

        for el in range(queue.size()):
            queue_elems += str(queue.dequeue())

        assert queue_elems == '3012'
