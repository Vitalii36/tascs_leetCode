"""Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
Example 4:

Input: nums = [1]
Output: [1]"""


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first_index = -1
        second_index = -1

        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                first_index = i

        if first_index == -1:
            nums.reverse()
            return

        for i in range(first_index + 1, len(nums)):
            if nums[first_index] < nums[i]:
                second_index = i

        nums[first_index], nums[second_index] = nums[second_index], nums[
            first_index]

        nums[first_index + 1:] = nums[first_index + 1:][::-1]