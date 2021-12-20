'''
Given an integer n, return true if it is a power
of three. Otherwise, return false.

An integer n is a power of three, if there exists
an integer x such that n == 3x.



Example 1:

Input: n = 27
Output: true
Example 2:

Input: n = 0
Output: false
Example 3:

Input: n = 9
Output: true
Example 4:

Input: n = 45
Output: false
'''


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0 or n < 0:
            return False
        import math
        if round(math.log(abs(n), 3), 12) % 1 == 0.0:
            return True
        return False
