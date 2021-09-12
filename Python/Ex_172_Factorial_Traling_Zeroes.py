'''
Given an integer n, return the number of trailing zeroes in n!.

Follow up: Could you write a solution that works in logarithmic time complexity?



Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Example 3:

Input: n = 0
Output: 0

'''


class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        res = 1
        for i in range(1, n + 1):
            res *= i
        fin = 0
        for j in str(res)[::-1]:
            if j != '0':
                break
            else:
                fin += 1
        return fin


result = Solution()
nums = 5
print(result.trailingZeroes(nums))
