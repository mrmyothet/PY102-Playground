class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head:
            current_node = self.head
            self.head = current_node.next
            current_node.next = None

        if self.head == None:
            self.tail = None

        return current_node.data

    # def enqueue(self, data):
    #     node = {"data": data, "next": None}
    #     if not self.has_elements():
    #         self.head = node
    #         self.tail = node
    #         return
    #     self.tail["next"] = node
    #     self.tail = node

    # def dequeue(self):
    #     if not self.has_elements():
    #         raise IndexError("dequeue from empty queue")
    #     removed = self.head
    #     self.head = removed["next"]
    #     if self.head is None:
    #         self.tail = None
    #     return removed["data"]

    def has_elements(self):
        return self.head != None

    def __repr__(self):
        items = []
        current = self.head
        while current is not None:
            items.append(current["data"])
            current = current["next"]
        return f"Queue({items})"


class PrinterTasks:
    def __init__(self):
        self.queue = Queue()

    def add_document(self, document):
        # Add the document to the queue
        self.queue.enqueue(document)

    def print_documents(self):
        # Iterate over the queue while it has elements
        while self.queue.has_elements():
            # Remove the document from the queue
            print("Printing", self.queue.dequeue())


printer_tasks = PrinterTasks()
# Add some documents to print
printer_tasks.add_document("Document 1")
printer_tasks.add_document("Document 2")
printer_tasks.add_document("Document 3")
# Print all the documents in the queue
printer_tasks.print_documents()
