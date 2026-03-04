# from dataclasses import dataclass


# @dataclass
class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node | None = None


class SinglyLinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            assert self.tail is not None
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

        if self.tail is None:
            self.tail = new_node

    def search(self, search_value):
        crt_node = self.head

        while crt_node is not None:
            if crt_node.data == search_value:
                return True

            crt_node = crt_node.next

        return False

    def insert(self, crt_data, new_data):
        host_node = self.search(crt_data)

        if host_node is not None:
            new_node = Node(new_data)

            new_node.next = host_node.next
            host_node.next = new_node

            return True

        return False

    def display(self):
        crt_node = self.head

        while crt_node is not None:
            print(crt_node.data, end=" -> ")
            crt_node = crt_node.next

        print("None")

    def reverseList(self, head: Node) -> Node:
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev
