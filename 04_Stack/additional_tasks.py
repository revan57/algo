import re
import operator

from Stack import Stack


# 5
def check_scopes_seq(string):
    stack = Stack()
    for letter in string:
        if letter == '(':
            stack.push('(')
        if letter == ')':
            if stack.pop() is None:
                return False

    if stack.size() == 0:
        return True

    return False


# 6
def count_postfix_expr(expression):
    def get_operator(op):
        operators = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }
        return operators[op]

    stack = Stack()
    expression = re.sub(r'[^\d+-/*=]', '', expression)
    for symbol in expression:
        if symbol.isdigit():
            stack.push(symbol)
        elif symbol == '=':
            return stack.pop()
        else:
            op = get_operator(symbol)
            el_1 = int(stack.pop())
            el_2 = int(stack.pop())
            stack.push(op(el_1, el_2))
