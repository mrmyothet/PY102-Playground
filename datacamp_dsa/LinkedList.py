class Node:
    def __init__(self, data):
        self.value = data
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def remove_at_beginning(self):
        if self.head:
            self.head = self.head.next
        else:
            self.head = None
            self.tail = None

    def display(self):
        current_node = self.head

        while current_node:
            print(current_node)
            current_node = current_node.next

        print("=" * 10)
