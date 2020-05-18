from SimpleQueue import SimpleQueue


# rotate queue on n elements
def rotate_queue(queue: SimpleQueue, n):
    if queue.size() > 0:
        for i in range(n):
            queue.enqueue(queue.dequeue())
