import timeit

code_to_test = """

class Solution:
    def reverse(self, x):
        i, num = 0, ''
        s = s.strip().split(' ')[0]
        while True:
            try:
                if s[i] != '-' and s[i] != '+':
                    int(s[:i+1])
                    num = s[:i+1]
                    i+=1
                else:
                    i += 1
            except:
                break
            if len(num) == len(s):
                break
        try:
            snum =int(num)
            if snum > 2147483647:
                return 2147483647
            elif snum < -2147483648:
                return -2147483648
            else:
                return snum
        except:
            return(0)

result = Solution()
x = 1534236469
print(result.reverse(x))
"""

elapsed_time = timeit.timeit(code_to_test, number=10)/10
print(elapsed_time)