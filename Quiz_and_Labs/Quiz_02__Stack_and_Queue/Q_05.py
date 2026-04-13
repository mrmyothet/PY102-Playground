"""
Assume that a stack class is already implemented with the usual stack operations.
The stack initially contains 5 elements.

Consider the following Python function, What happens when this function is executed?
"""


def process_stack(stack):
    result = []
    while not stack.is_empty():
        result.append(stack.peek())
    return result


"""

- The function returns a list containing the 5 elements in the same order.
- The function raises an error after processing all 5 elements.
- The function returns a list containing the 5 elements in reverse order.
- The function enters an infinite loop and never terminates.

"""
