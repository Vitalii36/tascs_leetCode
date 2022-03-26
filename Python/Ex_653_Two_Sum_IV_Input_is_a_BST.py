"""
Given the root of a Binary Search Tree and a target number k, return true if
there exist two elements in the BST such that their sum is equal to the given
target.

Example 1:


Input: root = [5,3,6,2,4,null,7], k = 9
Output: true
Example 2:


Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        output, stack = [root.val], [root.left, root.right]
        while stack:
            root = stack.pop()
            if root:
                output.append(root.val)
                stack.append(root.left)
                stack.append(root.right)
        for i, n in enumerate(output):
            if (k - n) in output and i != output.index(k - n):
                return True
        return False
