class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def _is_bst_helper(root, prev):

    if root is None:
        return True

    if not _is_bst_helper(root.left, prev):
        return False

    if prev[0] >= root.value:
        return False

    prev[0] = root.value
    return _is_bst_helper(root.right, prev)


def is_bst(root):
    prev = [float("-inf")]
    isbst_bool = _is_bst_helper(root, prev)
    return isbst_bool, prev


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(20)
root.left.left = TreeNode(3)
root.left.right = TreeNode(10)

root.right.left = TreeNode(11)
root.right.right = TreeNode(25)
is_bst(root)
