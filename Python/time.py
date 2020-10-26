import timeit

code_to_test = """
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
"""

elapsed_time = timeit.timeit(code_to_test, number=10)/10
print(elapsed_time)