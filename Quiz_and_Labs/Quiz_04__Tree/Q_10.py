def traversal(root):
    stack = []
    current = root
    out = []

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        out.append(current.value)
        current = current.right

    return out
