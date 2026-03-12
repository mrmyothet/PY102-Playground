# Implementing a Stack


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
            self.top = new_node
            self.size += 1

    def pop(self):
        if self.top is None:
            return None
        else:
            popped_node = self.top
            self.size -= 1
            self.top = self.top.next
            popped_node.next = None
            return popped_node.data
