from Deque import Deque


# check string is palindrome (ignore punctuation)
def is_palindrome(string: str):
    deque = Deque()
    processed_str = ''
    reversed_str = ''

    for s in string:
        if s.lower().isalpha():
            deque.addTail(s)
            processed_str += s

    while deque.size() > 0:
        reversed_str += deque.removeTail()

    return processed_str == reversed_str
