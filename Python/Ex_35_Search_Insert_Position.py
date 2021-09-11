"""Given a sorted array of distinct integers and a target value, return the index
if the target is found. If not, return the index where it would be if it were
inserted in order.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
Example 4:

Input: nums = [1,3,5,6], target = 0
Output: 0
Example 5:

Input: nums = [1], target = 0
Output: 0
"""


class Solution:
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        for i, n in enumerate(nums):
            if n > target:
                return i if i != 0 else 0
        return len(nums) if nums else 0

result = Solution()

nums = []
target = 0

print(result.searchInsert(nums, target))