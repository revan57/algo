from Deque import Deque


# check string is palindrome (ignore punctuation)
def is_palindrome(string: str):
    deque = Deque()

    for s in string:
        if s.lower().isalpha():
            deque.add_tail(s)

    while deque.size() > 0:
        if deque.remove_front() != deque.remove_tail():
            return False

    return True
