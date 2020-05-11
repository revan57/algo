from Deque import Deque


# check string is palindrome (ignore punctuation)
def is_palindrome(string: str):
    deque = Deque()

    for s in string:
        if s.lower().isalpha():
            deque.addTail(s)

    while deque.size() > 0:
        if deque.removeFront() != deque.removeTail():
            return False

    return True
