'''Given an array nums of n integers and an integer target, find three
integers in nums such that the sum is closest to target. Return the
sum of the three integers. You may assume that each input would have
exactly one solution.

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).'''


class Solution:
    def threeSumClosest(self, nums, target):
        min_diff, m_d_sum  = '', ''
        nums.sort()
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                tsum = nums[i] + nums[l] + nums[r]
                if min_diff == '':
                    min_diff = abs(tsum - target)
                    m_d_sum = tsum
                elif abs(tsum - target) < min_diff:
                    min_diff = abs(tsum - target)
                    m_d_sum = tsum
                if tsum < target:
                    l += 1
                elif tsum > target:
                    r -= 1
                else:
                    r -= 1
                    l += 1

        return(m_d_sum)

result = Solution()

ls = [-1,2,1,-4]


target = 1

print(result.threeSumClosest(ls, target))