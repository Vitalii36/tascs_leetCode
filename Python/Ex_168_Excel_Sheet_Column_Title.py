'''
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...


Example 1:

Input: columnNumber = 1
Output: "A"
Example 2:

Input: columnNumber = 28
Output: "AB"
Example 3:

Input: columnNumber = 701
Output: "ZY"
Example 4:

Input: columnNumber = 2147483647
Output: "FXSHRXW"
'''


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        import math
        f = ''
        s = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        while columnNumber > 0:
            val = columnNumber % 26
            if val:
                f = s[val] + f
            else:
                f = 'Z' + f
            if not val:
                columnNumber -= 26

            columnNumber //= 26
        return f


result = Solution()
columnNumber = 2147483647
print(result.convertToTitle(columnNumber))
