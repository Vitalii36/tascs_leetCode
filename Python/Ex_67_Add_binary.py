"""
Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""


class Solution:
    def addBinary(self, a, b):
        c = str(int(a)+int(b))
        while '2' in c:
            s = str()
            for i in c:
                if not s:
                    if i == '2':
                        s = '10'
                    else:
                        s = str(i)
                elif i == '2':
                    s = str(int(s)*10+10)
                else:
                    s = str(int(s)*10+int(i))
            c = s
        if not c:
            c = "0"
        return c


result = Solution()

a = "0"
b = "1"

print(result.addBinary(a, b))