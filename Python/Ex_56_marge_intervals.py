"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and
return an array of the non-overlapping intervals that cover all the intervals in the input.



Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        f_elem, result = intervals[0], []
        intervals = intervals[1:]
        while intervals:
            if f_elem[1] >= intervals[0][0]:
                f_elem = [min(f_elem[0], intervals[0][0]), max(f_elem[1], intervals[0][1])]
                intervals = intervals[1:]
            else:
                result.append(f_elem)
                f_elem = intervals[0]
                intervals = intervals[1:]
        if f_elem:
            result.append(f_elem)
        return result
