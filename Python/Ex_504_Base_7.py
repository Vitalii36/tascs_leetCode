'''
Given an integer num, return a string of its base 7 representation.



Example 1:

Input: num = 100
Output: "202"
Example 2:

Input: num = -7
Output: "-10"


Constraints:

-107 <= num <= 107
'''


class Solution:
    def convertToBase7(self, num: int) -> str:
        b, j, s = 7, '', ''
        if num == 0:
            return '0'
        if num < 0:
            num = abs(num)
            j = '-'
        while num:
            s = s + str(int(num % b))
            num //= b
        return j + s[::-1]
