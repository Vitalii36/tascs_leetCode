"""Given a linked list, swap
every two adjacent nodes and
return its head.

Example
1:

Input: head = [1, 2, 3, 4]
Output: [2, 1, 4, 3]
Example
2:

Input: head = []
Output: []
Example
3:

Input: head = [1]
Output: [1]"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        l = []

        while (head):
            l.append(head.val)
            head = head.next

        for i in range(len(l)):
            if i % 2 == 1:
                l[i], l[i - 1] = l[i - 1], l[i]

        i = ListNode()
        temp = i
        for j in l:
            i.next = ListNode(j)
            i = i.next
        return temp.next
