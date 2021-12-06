'''
Given the root of a binary tree, return all
root-to-leaf paths in any order.

A leaf is a node with no children.



Example 1:


Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
Example 2:

Input: root = [1]
Output: ["1"]


Constraints:

The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        def dfs(node, path):
            if not node:
                return []

            if not node.left and not node.right:
                path.append(str(node.val))
                leaf_string = "".join(path)
                path.pop()
                return [leaf_string]

            total_paths = []

            path.append(f"{str(node.val)}->")

            total_paths.extend(dfs(node.left, path))
            total_paths.extend(dfs(node.right, path))

            path.pop()

            return total_paths

        return dfs(root, [])