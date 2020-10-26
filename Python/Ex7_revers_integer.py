'''Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store
integers within the 32-bit signed integer range: [−231,  231 − 1].
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0
'''


class Solution:
    def reverse(self, x):
        if x < 2147483647 and x > -2147483648:
            s = ''
            if x < 0:
                s+= '-'
                x*=-1
            for i in range(len(str(x))-1,-1,-1):
                s = s + str(x)[i]
            return(int(s) if int(s) < 2147483647 and int(s) > -2147483648 else 0)
        else:
            return (0)

result = Solution()
x = 1534236469
print(result.reverse(x))