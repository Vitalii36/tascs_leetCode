'''
We have to time interval in float type
Example 8.00 - 22.00 and 21.00 - 6.00
We need value of hours between to interval

Ex 1
8.00 22.00 21.00 6.00
Out=1.00
or
6.00 - 14.00
'''


class Solution:
    def isTimeValue(self, t1, t2, t3, t4):
        if t2 < t1 and t4 < t3:
            t4 = 24 + t4
            t2 += 24 + t2
        elif t2 < t1:
            t2 += t1
        elif t4 < t3:
            t4 += t3
        print(t1, t2, t3, t4)
        h_from = t1 if t1 > t3 else t3
        h_to = t2 if t2 < t4 else t4
        print(h_from, h_to)
        return h_to - h_from




result = Solution()
t1, t2, t3, t4 = 8.0, 12.0, 22.0, 6.0
# t1, t2, t3, t4 = 5.0, 22.0, 6.0, 23.0
# t1, t2, t3, t4 = 22.0, 9.0, 6.0, 23.0
# t1, t2, t3, t4 = 8.0, 22.0, 21.0, 6.0
# t1, t2, t3, t4 = 22.0, 8.0, 21.0, 6.0
# t1, t2, t3, t4 = 22.0, 23.0, 22.0, 6.0

print(result.isTimeValue(t1, t2, t3, t4))
