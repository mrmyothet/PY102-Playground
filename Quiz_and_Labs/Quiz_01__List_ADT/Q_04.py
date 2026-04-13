"""
Assume that the list is given as: List: 16 -> 22 -> 83 -> 49 -> None, use the following code and answer the questions.

prev = None
curr = head

while curr != None:
    next_node = curr.next
    curr.next = prev
    prev = curr
    curr = next_node

head = prev
After the first loop iteration,

prev.next is pointing to
None

curr.data is
22

After the whole while loop, head has value of
49
  and head.next is pointing to
83

"""
