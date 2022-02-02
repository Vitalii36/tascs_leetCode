'''
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root
 node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal,
 each group of children is separated by the null value (See examples).



Example 1:



Input: root = [1,null,3,2,4,null,5,6]
Output: 3
Example 2:



Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: 5


Constraints:

The total number of nodes is in the range [0, 104].
The depth of the n-ary tree is less than or equal to 1000.
'''


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def isLeaf(self, node):
        return node.children == []

    def maxDepth(self, root: 'Node') -> int:
        if root == None:
            return 0

        stack = []
        checked = {}
        count = 0
        checked[root] = 1
        stack.append(root)

        while stack != []:
            current = stack.pop()

            if self.isLeaf(current):
                count = max(count, checked[current])
            else:
                for i in current.children:
                    if i not in checked:
                        stack.append(i)
                        checked[i] = checked[current] + 1
        return count
