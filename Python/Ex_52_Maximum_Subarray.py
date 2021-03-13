"""
Given an integer array nums, find the contiguous subarray (containing at
least one number) which has the largest sum and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
"""


class Solution:
    def maxSubArray(self, nums):
        max = sum(nums)
        while len(nums) > 1:
            if sum(nums[:-1]) < sum(nums[1:]):
                if max < sum(nums[1:]):
                    max = sum(nums[1:])
                nums = nums[1:]
            else:
                if max < sum(nums[:-1]):
                    max = sum(nums[:-1])
                nums = nums[:-1]
        return max


result = Solution()

nums = [1,2,-1,-2,2,1,-2,1,4,-5,4]

print(result.maxSubArray(nums))