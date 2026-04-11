def bst_search_iterative(root, target):
    current = root
    count = 0
    while current:
        count += 1
        print(count)
        if target == current.value:
            return True
        elif target < current.value:
            current = current.left
        else:
            current = current.right

    return False
