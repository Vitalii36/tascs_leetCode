'''
Given a positive integer num, write a function
which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.


Example 1:

Input: num = 16
Output: true
Example 2:

Input: num = 14
Output: false


Constraints:

1 <= num <= 2^31 - 1
'''


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        a = int((len(str(num)) // 2 + len(str(num)) % 2) * '9')
        while a != 0:
            if a * a == num:
                return True
            else:
                a -= 1
        return False


result = Solution()
nums1 = 2147483632

print(result.isPerfectSquare(nums1))
