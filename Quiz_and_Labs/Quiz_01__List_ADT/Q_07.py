"""
Assume that the link is given as : A <-> B <-> C <-> D, using the below code, what sequence is printed?

curr = head
while curr.next != None:
    curr = curr.next

while curr != None:
    print(curr.data)
    curr = curr.prev
Question 7Answer

A B C D


D C B A


"""
