import queue

book_stack = queue.LifoQueue(maxsize=0)

book_stack.put("Atomic Habits")
book_stack.get()
