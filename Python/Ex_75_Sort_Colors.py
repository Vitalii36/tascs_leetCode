"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color
are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.



Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]


Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
"""

# insertionSort
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def insertionSort(A):

            for i in range(1, len(A)):

                value = A[i]
                j = i

                while j > 0 and A[j - 1] > value:
                    A[j] = A[j - 1]
                    j = j - 1

                A[j] = value

        return insertionSort(nums)

# countsort
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def countsort(A, k):

            output = [0] * len(A)

            freq = [0] * (k + 1)

            for i in A:
                freq[i] = freq[i] + 1

            total = 0
            for i in range(k + 1):
                oldCount = freq[i]
                freq[i] = total
                total += oldCount

            for i in A:
                output[freq[i]] = i
                freq[i] = freq[i] + 1

            for i in range(len(A)):
                A[i] = output[i]

        return countsort(nums, 2)

# heapsort
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def LEFT(i):
            return 2 * i + 1

        def RIGHT(i):
            return 2 * i + 2

        def swap(A, i, j):
            temp = A[i]
            A[i] = A[j]
            A[j] = temp

        def heapify(A, i, size):
            left = LEFT(i)
            right = RIGHT(i)

            largest = i

            if left < size and A[left] > A[i]:
                largest = left

            if right < size and A[right] > A[largest]:
                largest = right

            if largest != i:
                swap(A, i, largest)
                heapify(A, largest, size)

        def pop(A, size):
            if size <= 0:
                return -1

            top = A[0]

            A[0] = A[size - 1]

            heapify(A, 0, size - 1)

            return top

        def heapsort(A):

            n = len(A)

            i = (n - 2) // 2
            while i >= 0:
                heapify(A, i, n)
                i = i - 1
            while n:
                A[n - 1] = pop(A, n)
                n = n - 1

        return heapsort(nums)