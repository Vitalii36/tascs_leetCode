"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
(i.e., from left to right, then right to left for the next level and alternate between).

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        zig, res, l_root = True, [[root.val]], [root.left, root.right]
        while l_root:
            l_new, r_new = [], []
            for l in l_root:
                if l:
                    r_new.append(l.val)
                    l_new.extend([l.left, l.right])
            if l_new:
                l_root = l_new
                if zig:
                    r_new.reverse()
                    zig = False
                else:
                    zig = True
                res.append(r_new)
            else:
                break
        return res