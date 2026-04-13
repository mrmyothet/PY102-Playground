"""
Assume that the stack class is already implemented and follows the LIFO principle.
What will be printed by the following code?

"""

from numpy import stack


def function_example(s):
    stack_eg = stack()
    for ch in s:
        stack_eg.push(ch)

    result = ""
    while not stack_eg.is_empty():
        result += stack_eg.peek()
        stack_eg.pop()

    return result


function_example("5678")
