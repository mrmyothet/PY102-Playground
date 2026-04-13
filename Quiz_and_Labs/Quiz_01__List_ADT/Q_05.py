"""
Assume that the list is given as: List: 16 -> 22 -> 83 -> 49 -> None, use the following code and answer the questions.

curr = head
count = 0

while curr != None:
    if count == 2:
        print(curr.data)
        break
    count = count + 1
    curr = curr.next
After the code is runned,
83
  is printed, and curr is point to
49

"""
