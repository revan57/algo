from Queue import Queue


# rotate queue on n elements
def rotate_queue(queue: Queue, n):
    if queue.size() > 0:
        for i in range(n):
            queue.enqueue(queue.dequeue())
