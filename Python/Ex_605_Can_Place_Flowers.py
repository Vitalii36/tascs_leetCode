'''
You have a long flowerbed in which some of the plots are planted, and some are
not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty
and 1 means not empty, and an integer n, return if n new flowers can be planted
in the flowerbed without violating the no-adjacent-flowers rule.



Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false


Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
'''


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not n:
            return True
        if len(flowerbed) == 1:
            return True if not flowerbed[0] and n == 1 else False
        n_c, i = 0, 0
        f = 1 if not flowerbed[0] else 0
        while i < len(flowerbed) - 1:
            if not flowerbed[i] and not f:
                f = 1
            elif not flowerbed[i] and f and not flowerbed[i + 1]:
                f = 0
                n_c += 1
                flowerbed[i] = 1
            elif flowerbed[i]:
                f = 0
            i += 1
        if not flowerbed[-1] and not flowerbed[-2]:
            n_c += 1
        return True if n_c >= n else False
