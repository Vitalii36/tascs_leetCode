"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.



Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].


Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105
"""


class Solution(object):
    def marge_overlapping(self, interval, newInterval):
        return [min([interval[0], newInterval[0]]),
                max([interval[-1], newInterval[-1]])]

    def check_overlapping(self, interval, newInterval):
        if newInterval[0] <= interval[0] <= newInterval[-1] or newInterval[0] <= \
                interval[-1] <= newInterval[-1] or interval[0] <= newInterval[
            0] <= interval[-1] or interval[0] <= newInterval[-1] <= interval[
            -1]:
            return True
        return False

    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0:
            return [newInterval]
        first_elem_inx = [i[0] for i in intervals]

        if newInterval[0] in first_elem_inx:
            intervals.insert(first_elem_inx.index(newInterval[0]), newInterval)
        else:
            for i in first_elem_inx:
                if i >= newInterval[0]:
                    intervals.insert(first_elem_inx.index(i), newInterval)
                elif i < newInterval[0]:
                    continue
            if newInterval not in intervals:
                intervals.append(newInterval)

        result, head_arr, is_added = [], intervals[0], False
        for interval in intervals[1:]:

            if self.check_overlapping(interval=head_arr, newInterval=interval):
                head_arr = self.marge_overlapping(interval=head_arr,
                                                  newInterval=interval)
            else:
                result.append(head_arr)
                head_arr = interval
        result.append(head_arr)
        return result
