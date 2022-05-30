"""
Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different
nodes in the tree.



Example 1:


Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1


Constraints:

The number of nodes in the tree is in the range [2, 100].
0 <= Node.val <= 105
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        l_tree = [root.val]
        root = [root.left, root.right]
        while root:
            val = root.pop()
            if val:
                l_tree.append(val.val)
                root.append(val.left)
                root.append(val.right)
        l_tree = list(set(l_tree))
        res = False
        l_tree.sort()
        if len(l_tree) == 1:
            return l_tree
        for i in range(len(l_tree) - 1):
            diff = abs(l_tree[i] - l_tree[i + 1])
            if not res:
                res = diff
            elif res > diff:
                res = diff
        return res
