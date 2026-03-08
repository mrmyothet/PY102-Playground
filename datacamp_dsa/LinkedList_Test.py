from LinkedList import LinkedList, Node

l_list = LinkedList()
n1 = Node(70)
n2 = Node(80)
n3 = Node(90)
l_list.insert_at_beginning(n1)
l_list.insert_at_beginning(n2)
l_list.insert_at_beginning(n3)
l_list.display()

l_list.remove_at_beginning()
l_list.display()
