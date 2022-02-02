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


        # if t1 < t2 and t3 > t4 and ((t3 <= t2 <= 24 or 0 <= t2 <= t4) or (t3 <= t1 <= 24 or 0 <= t1 <= t4)):
        #     if t1 < t3 and t2 > t4:
        #         if t2 > t3:
        #             return t2 - t3
        #         elif t4 > t1:
        #             return 24 - t3 + t4
        #         return 24 - t3 + t1
        #     elif t1 > t3 and t2 > t4:
        #         return t2 - t1
        #     elif t1 < t3 and t2 < t4:
        #         return t2 - t1
        #
        # elif t1 < t2 and t3 < t4 and ((t3 <= t2 <= t4) or (t3 <= t1 <= t4)):
        #     if t1 >= t3 and t2 <= t4:
        #         return t2 - t1
        #     elif t1 <= t3 and t2 <= t4:
        #         return t2 - t3
        #     elif t1 >= t3 and t2 >= t4:
        #         return t4 - t1
        #     else:
        #         t4 - t2
        # elif t1 > t2 and t3 < t4 and ((t3 <= t2 <= 24 and 0 < t2 <= t4) or (t3 <= t1 <= 24 and 0 < t1 <= t4)):
        #     if t2 >= t3 and t1 <= t4:
        #         return t2 - t1
        #     elif t2 >= t3 and t1 >= t4:
        #         return t2 - t4
        # elif t1 > t2 and t3 > t4:
        #     if t2 <= t4 and t1 >= t3:
        #         return 24 - t1 + t2
        #     elif t2 <= t4 and t1 <= t3:
        #         return 24 - t3 + t2
        #     elif t2 >= t4 and t1 <= t3:
        #         return 24 - t3 + t4
        #     elif t2 >= t4 and t1 >= t3:
        #         return 24 - t1 + t4



class Solution:
    def isTimeValue(self, t1, t2, t3, t4):
        if t1 >= t2 and t3 >= t4:
            print(111, t1,t2,t3,t4)
            if t3 >= t2 >= t4 or t3 >= t1 >= t4:
                t2 += 24
                t4 += 24
                l = [t1, t2, t3, t4]
                l.sort()
                print(l)
                return l[2] - l[1]
        if t1 >= t2 and t3 <= t4:
            print(222, t1,t2,t3,t4)
            if t3 <= t2 <= t4 or t3 <= t1 <= t4:
                t2 += 24
                t3 += 24
                t4 += 24
                l = [t1, t2, t3, t4]
                l.sort()
                print(l)
                return l[2] - l[1]
        if t1 <= t2 and t3 <= t4:
            print(333, t1,t2,t3,t4)
            if t3 <= t2 <= t4 or t3 <= t1 <= t4:
                l = [t1, t2, t3, t4]
                l.sort()
                print(l)
                return l[2] - l[1]
# t1, t2, t3, t4 = 0.0, 3.0, 22.0, 6.0 # 3
        if t1 <= t2 and t3 >= t4:
            d = 0
            if t2 > t3:
                d += t2 - t3
            if t1 <= t4 and t2 >= t4:
                d += t4 - t1
            if t1 <= t4 and t2 <= t4:
                d += t2 - t1
            return d

result = Solution()
# t1, t2, t3, t4 = 8.0, 12.0, 22.0, 6.0 # none
# t1, t2, t3, t4 = 5.0, 22.0, 6.0, 23.0 # 16
# t1, t2, t3, t4 = 2.0, 9.0, 6.4, 23.23 # 2.6
# t1, t2, t3, t4 = 8.0, 22.0, 21.0, 6.0 # 1 !!
# t1, t2, t3, t4 = 4.0, 22.0, 21.0, 6.0 # 1 !!
# t1, t2, t3, t4 = 21.0, 22.0, 20.0, 6.0 # 1 !!
# t1, t2, t3, t4 = 22.0, 8.0, 21.0, 6.0 # 8
# t1, t2, t3, t4 = 15.0, 0.0, 22.0, 6.0 # 2
# t1, t2, t3, t4 = 8.0, 14.0, 22.0, 6.0 # 0
# t1, t2, t3, t4 = 0.0, 3.0, 22.0, 6.0 # 3
# t1, t2, t3, t4 = 3.0, 8.0, 9.0, 12.0 # none
# t1, t2, t3, t4 = 8.0, 14.0, 22.0, 6.0 # 2
# t1, t2, t3, t4 = 1.0, 2.0, 22.0, 6.0 # 1 !!
# t1, t2, t3, t4 = 7.0, 24.0, 22.0, 6.0 # 15 !!
# t1, t2, t3, t4 = 7.0, 20.0, 22.0, 6.0 # 15 !!
# t1, t2, t3, t4 = 23.0, 2.0, 22.0, 6.0 # 3
t1, t2, t3, t4 = 22.0, 1.0, 4.0, 1.0 # 3
# t1, t2, t3, t4 = 22.0, 2.0, 22.0, 1.0 # 8
# t1, t2, t3, t4 = 14.0, 8.0, 22.0, 6.0 # 8
# t1, t2, t3, t4 = 4.0, 8.0, 22.0, 6.0 # 2
# t1, t2, t3, t4 = 0.0, 15.0, 22.0, 6.0 # 6
# t1, t2, t3, t4 = 0.0, 15.0, 15.0, 6.0 # 6
# t1, t2, t3, t4 = 0.0, 15.0, 0.0, 14.0 # 14

print(result.isTimeValue(t1, t2, t3, t4))
