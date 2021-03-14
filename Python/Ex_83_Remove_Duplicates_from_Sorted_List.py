"""
Given the head of a sorted linked list, delete all duplicates such that
each element appears only once. Return the linked list sorted as well

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        l = []
        while (head):
            l.append(head.val)
            head = head.next
        l = list(set(l))
        l.sort()
        i = ListNode()
        temp = i
        for j in l:
            i.next = ListNode(j)
            i = i.next
        return temp.next

result = Solution()

head = [-1,0,0,0,0,3,3]

print(result.deleteDuplicates(head))