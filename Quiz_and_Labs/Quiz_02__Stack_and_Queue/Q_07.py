"""
Assume that the stack class is already implemented and follows the LIFO principle.
What will be printed by the following code?


"""

from numpy import stack


stack01 = stack()

stack01.push(23)
stack01.push(65)
stack01.push(82)
stack01.pop()
print(stack01.peek())
