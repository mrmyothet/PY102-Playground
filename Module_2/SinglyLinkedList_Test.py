from SinglyLinkedList import SinglyLinkedList

linked_list = SinglyLinkedList()
linked_list.append(70)
linked_list.append(85)
linked_list.append(90)

linked_list.display()

linked_list.insert_at_beginning(60)
linked_list.display()

reverse_sll = SinglyLinkedList()
reverse_sll.append(1)
reverse_sll.append(2)
reverse_sll.append(3)
reverse_sll.append(4)
reverse_sll.append(5)

reverse_sll.head = reverse_sll.reverseList(reverse_sll.head)
reverse_sll.display()