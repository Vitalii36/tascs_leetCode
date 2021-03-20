"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e.,
 symmetric around its center).

 Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        stack = [root.right, root.left]
        while stack:
            left = stack.pop()
            right = stack.pop()
            if left is None and right is None:
                pass
            elif left is None or right is None or left.val != right.val:
                return False
            else:
                stack.append(right.right)
                stack.append(left.left)
                stack.append(right.left)
                stack.append(left.right)
        return True


result = Solution()

# print(result.isSameTree(root))
