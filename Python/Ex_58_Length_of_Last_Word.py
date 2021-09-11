"""
Given a string s consists of some words separated by spaces, return
the length of the last word in the string. If the last word does not exist,
return 0.

A word is a maximal substring consisting of non-space characters only.

Example 1:

Input: s = "Hello World"
Output: 5
Example 2:

Input: s = " "
Output: 0
"""


class Solution:
    def lengthOfLastWord(self, s):
        s=s.strip()
        return len(s[s.rfind(" ")+1:])

# class Solution:
#     def lengthOfLastWord(self, s):
#         l = s.split(' ')
#         p =''
#         while p in l:
#             l.remove(p)
#         print(l)
#         if l:
#             return len(l[-1])
#         else:
#             return 0

result = Solution()

s = " a "

print(result.lengthOfLastWord(s))