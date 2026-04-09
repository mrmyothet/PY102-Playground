import unittest
from typing import Optional, List

from lab05 import TreeNode, sorted_array_to_bst


# --- Test Helper Functions ---
def height(node: Optional[TreeNode]) -> int:
    if not node:
        return 0
    return 1 + max(height(node.left), height(node.right))


def is_balanced(node: Optional[TreeNode]) -> bool:
    if not node:
        return True
    left_height = height(node.left)
    right_height = height(node.right)
    if abs(left_height - right_height) > 1:
        return False
    return is_balanced(node.left) and is_balanced(node.right)


def is_valid_bst(
    node: Optional[TreeNode], min_val=float("-inf"), max_val=float("inf")
) -> bool:
    if not node:
        return True
    if not (min_val < node.value < max_val):
        return False
    return is_valid_bst(node.left, min_val, node.value) and is_valid_bst(
        node.right, node.value, max_val
    )


# --- The 10 Unique Test Cases ---
class TestSortedArrayToBST(unittest.TestCase):

    def verify_tree(self, nums):
        """Helper to run the function and assert BST properties."""
        root = sorted_array_to_bst(nums)
        self.assertTrue(is_balanced(root), f"Tree is not balanced for input: {nums}")
        self.assertTrue(
            is_valid_bst(root), f"Tree is not a valid BST for input: {nums}"
        )

        # Verify no elements were lost by checking the size
        def count_nodes(node):
            return 1 + count_nodes(node.left) + count_nodes(node.right) if node else 0

        self.assertEqual(
            count_nodes(root), len(nums), "Tree node count does not match array length"
        )

    # 1. Edge Case: Empty array
    def test_empty_array(self):
        self.assertIsNone(sorted_array_to_bst([]))

    # 2. Base Case: Single element
    def test_single_element(self):
        self.verify_tree([5])

    # 3. Even Number of Elements (Small): Tests left/right bias handling
    def test_two_elements(self):
        self.verify_tree([1, 2])

    # 4. Odd Number of Elements (Perfectly Balanced)
    def test_three_elements(self):
        self.verify_tree([1, 2, 3])

    # 5. Even Number of Elements (Larger): Forces one subtree to be taller by exactly 1
    def test_even_length_array(self):
        self.verify_tree([1, 2, 3, 4, 5, 6, 7, 8])

    # 6. Mixed Signs: Standard array with negative, zero, and positive numbers
    def test_mixed_signs(self):
        self.verify_tree([-10, -3, 0, 5, 9])

    # 7. All Negative Numbers: Ensures correct handling of negative values
    def test_all_negatives(self):
        self.verify_tree([-50, -40, -30, -20, -10, -5])

    # 8. Large Gaps: Tests numbers with massive gaps between values
    def test_large_gaps(self):
        self.verify_tree([1, 100, 10000, 1000000])

    # 9. Complete Tree Level: Size that perfectly fills all levels (e.g., 7 nodes = 3 full levels)
    def test_perfectly_filled_levels(self):
        self.verify_tree([10, 20, 30, 40, 50, 60, 70])

    # 10. Extreme Boundaries: Tests with Python's larger integer capabilities
    def test_extreme_values(self):
        self.verify_tree([-1000000000, 0, 1000000000])


if __name__ == "__main__":
    unittest.main()
