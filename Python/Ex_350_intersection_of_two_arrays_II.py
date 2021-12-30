'''
Given two integer arrays nums1 and nums2, return an array of
their intersection. Each element in the result must appear as
many times as it shows in both arrays and you may return the
result in any order.



Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.

'''


class Solution:
    def intersec(self, nums1, nums2):
        nums_1, nums_2, res = list(set(nums1)), list(set(nums2)), []
        start = nums_1 if len(nums_1) < len(nums_2) else nums_2
        second = nums_2 if len(nums_1) < len(nums_2) else nums_1
        print(start, second)
        for obj in start:
            if obj in second:
                count = nums1.count(obj) if nums1.count(obj) < nums2.count(obj) else nums2.count(obj)
                for i in range(count):
                    res.append(obj)
        return res


result = Solution()
nums1, nums2 = [1, 2, 2, 1], [2, 2]

print(result.intersec(nums1, nums2))
