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
