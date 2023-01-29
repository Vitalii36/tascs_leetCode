"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]


Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []

        def solve(nums, j):
            if j == n:
                ans.append(nums[:])
            for i in range(j, n):
                nums[i], nums[j] = nums[j], nums[i]
                solve(nums, j + 1)
                nums[i], nums[j] = nums[j], nums[i]

        solve(nums, 0)
        return ans
