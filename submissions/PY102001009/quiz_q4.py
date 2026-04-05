class TreeNode:
    def __init__(self, value: int, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def _is_bst_helper(root, prev):

    if root is None:
        return True

    if not _is_bst_helper(root.left, prev):
        return False

    if prev >= root.value:
        return False

    prev = root.value
    return _is_bst_helper(root.right, prev)


def is_bst(root):
    prev = float("-inf")
    isbst_bool = _is_bst_helper(root, prev)
    return isbst_bool, prev


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.right = TreeNode(3)
print(is_bst(root))
