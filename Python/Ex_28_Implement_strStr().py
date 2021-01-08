"""mplement strStr().
Return the index of the first occurrence of needle
in haystack, or -1 if needle is not part of haystack.
Clarification:
What should we return when needle is an empty string?
 This is a great question to ask during an interview.
For the purpose of this problem, we will return 0
when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Example 3:

Input: haystack = "", needle = ""
Output: 0"""


class Solution:
    def strStr(self, haystack, needle):
        if needle == haystack or needle == '':
            return 0
        if needle not in haystack:
            return -1
        i = 0
        ln = len(needle)
        while len(haystack)+1 > ln:
            if haystack[i:ln] == needle:
                return i
            else:
                i+=1
                ln+=1



result = Solution()

n = 'abc'
v = 'c'
print(result.strStr(n, v))