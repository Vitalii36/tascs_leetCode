'''
Given the root of a binary tree, return the
inorder traversal of its nodes' values.

Example 1:

Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
Example 4:

Input: root = [1,2]
Output: [2,1]
Example 5:

Input: root = [1,null,2]
Output: [1,2]

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def inorderTraversal(self, root):

        if not root:
            return []
        val, stack = [], []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            l = stack.pop()
            val.append(l.val)
            node = l.right
        return val


result = Solution()
root = [1, 2]
print(result.inorderTraversal(root))
