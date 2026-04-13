"""
Assume that the list is given as: List: 16 -> 22 -> 83 -> 49 -> None, use the following code and answer the questions.

prev = None
curr = head

while curr is not None and curr.data !=49:
    prev = curr
    curr = curr.next

if curr is not None:
    if prev is None:
        head = curr.next
    else:
        prev.next = curr.next
prev.next is pointing to
None

the new list has
3
  elements
the node
49
  is removed.
"""
