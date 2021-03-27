"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
Example 3:

Input: root = []
Output: 0
Example 4:

Input: root = [0]
Output: 1
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        stack_2 = []
        if root:
            stack = [root.left, root.right]
            count = 1
        else:
            return 0
        while stack:
            left = stack.pop()
            right = stack.pop()
            if left == None and right == None:
                pass
            elif left != None and right != None:
                stack_2.append(right.right)
                stack_2.append(left.left)
                stack_2.append(right.left)
                stack_2.append(left.right)
            elif  left != None:
                stack_2.append(left.left)
                stack_2.append(left.right)
            elif  right != None:
                stack_2.append(right.right)
                stack_2.append(right.left)
            if not stack and stack_2:
                stack = stack_2
                stack_2 =[]
                count+=1
        return coun

result = Solution()

# print(result.isSameTree(root))
