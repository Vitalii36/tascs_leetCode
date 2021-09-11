"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in
height by no more than 1

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true

"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root):
        def height(root):
            if not root:
                return 0
            left_height = height(root.left)
            if left_height == -1:
                return -1
            right_height = height(root.right)
            if right_height == -1:
                return -1
            return max(left_height, right_height) + 1 if abs(left_height - right_height) <= 1 else -1

        return height(root) != -1


result = Solution()
nums = [3, 9, 20, null, null, 15, 7]
print(result.isBalanced(nums))