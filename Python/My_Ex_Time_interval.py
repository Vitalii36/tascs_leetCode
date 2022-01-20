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
from datetime import datetime, timedelta


class Solution:
    def isTimeValue(self, t1, t2, t3, t4):
        if t1 < t2 and t3 > t4 and ((t3 <= t2 <= 24 or 0 < t2 <= t4) or (t3 <= t1 <= 24 or 0 < t1 <= t4)):
            if t1 < t3 and t2 > t4:
                return t2 - t3
            elif t1 > t3 and t2 > t4:
                return t2 - t1
            elif t1 < t3 and t2 < t4:
                return t2 - t1

        elif t1 < t2 and t3 < t4 and ((t3 <= t2 <= t4) or (t3 <= t1 <= t4)):
            if t1 > t3 and t2 < t4:
                return t2 - t1
            elif t1 < t3 and t2 < t4:
                return t2 - t3
            elif t1 > t3 and t2 > t4:
                return t4 - t1
            else:
                t4 - t2
        elif t1 > t2 and t3 < t4 and ((t3 <= t2 <= 24 and 0 < t2 <= t4) or (t3 <= t1 <= 24 and 0 < t1 <= t4)):
            if t2 > t3 and t1 < t4:
                return t2 - t1
            elif t2 > t3 and t1 > t4:
                return t2 - t4
        elif t1 > t2 and t3 > t4 and ((t2 <= t4) or (t1 >= t3)):
            if t2 < t4 and t1 > t3:
                return 24 - t1 + t2
            elif t2 < t4 and t1 < t3:
                return 24 - t3 + t2
            elif t2 > t4 and t1 < t3:
                return 24 - t3 + t4
            elif t2 > t4 and t1 > t3:
                return 24 - t1 + t4


result = Solution()
# t1, t2, t3, t4 = 8.0, 12.0, 22.0, 6.0
# t1, t2, t3, t4 = 5.0, 22.0, 6.0, 23.0
# t1, t2, t3, t4 = 2.0, 9.0, 6.4, 23.23
# t1, t2, t3, t4 = 8.0, 22.0, 21.0, 6.0
# t1, t2, t3, t4 = 22.0, 8.0, 21.0, 6.0
# t1, t2, t3, t4 = 15.0, 24.0, 22.0, 6.0
# t1, t2, t3, t4 = 1.0, 2.0, 22.0, 6.0
# t1, t2, t3, t4 = 23.0, 2.0, 22.0, 6.0
t1, t2, t3, t4 = 15.0, 3.0, 22.0, 6.0

print(result.isTimeValue(t1, t2, t3, t4))
