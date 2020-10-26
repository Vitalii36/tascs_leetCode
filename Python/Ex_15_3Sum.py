'''Given an array nums of n integers, are there elements a, b, c in
nums such that a + b + c = 0? Find all unique triplets in the array
which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
'''


class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = set()
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                tsum = nums[i] + nums[l] + nums[r]
                if tsum < 0:
                    l += 1
                elif tsum > 0:
                    r -= 1
                else:
                    result.add((nums[i], nums[l], nums[r]))
                    r -= 1
                    l += 1
        return result

result = Solution()
x = [-1,0,1,2,-1,-4]
print(result.threeSum(x))