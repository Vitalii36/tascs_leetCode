'''Merge two sorted linked lists and return it as a new sorted list.
The new list should be made by splicing together the nodes of the
first two lists.

Example 1:

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: l1 = [], l2 = []
Output: []
Example 3:

Input: l1 = [], l2 = [0]
Output: [0]'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l = []

        while (l1):
            l.append(l1.val)
            l1 = l1.next

        while (l2):
            l.append(l2.val)
            l2 = l2.next

        l.sort()
        i = ListNode()
        temp = i
        for j in l:
            i.next = ListNode(j)
            i = i.next
        return temp.next