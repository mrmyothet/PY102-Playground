def traversal(root):
    if not root:
        return []
    stack = [root]
    out = []
    while stack:
        node = stack.pop()
        out.append(node.value)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return out
