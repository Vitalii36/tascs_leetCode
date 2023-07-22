"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it
can trap after raining.



Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case,
6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9


Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(set(height)) == 1:
            return 0
        res, i = 0, 0
        while i < len(height):
            left = height[:i]
            right = height[i:]
            max_left = max(left) if left else 0
            max_right = max(right) if right else 0
            num = max_left if max_left < max_right else max_right
            res += num - height[i] if num > height[i] else 0
            i += 1
        return res
