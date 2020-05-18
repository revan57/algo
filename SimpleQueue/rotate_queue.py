from Queue import SImpleQueue


# rotate queue on n elements
def rotate_queue(queue: SImpleQueue, n):
    if queue.size() > 0:
        for i in range(n):
            queue.enqueue(queue.dequeue())
