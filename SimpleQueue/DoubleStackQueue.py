import inspect
import os
import sys

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from Stack.Stack import Stack


class DoubleStackQueue:
    def __init__(self):
        self.queue = Stack()
        self.buffer = Stack()

    def enqueue(self, item):
        self.buffer.push(item)

    def dequeue(self):
        while self.buffer.size() > 0:
            self.queue.push(self.buffer.pop())

        val = self.queue.pop() if self.queue else None

        while self.queue.size() > 0:
            self.buffer.push(self.queue.pop())

        return val

    def size(self):
        return self.buffer.size()
