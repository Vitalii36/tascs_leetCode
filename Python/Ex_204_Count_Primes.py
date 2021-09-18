'''
Count the number of prime numbers less than a non-negative number, n.


Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
'''
from math import sqrt


class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        numbers = {}
        for p in range(2, int(sqrt(n)) + 1):
            if p not in numbers:
                for multiple in range(p*p, n, p):
                    numbers[multiple] = 1
        return n - len(numbers) - 2
    # test
