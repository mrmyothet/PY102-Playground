class TreeNode:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left_child = left
        self.right_child = right


node1 = TreeNode("B")
node2 = TreeNode("C")
root_node = TreeNode("A", node1, node2)
