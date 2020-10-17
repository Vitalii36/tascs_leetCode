import timeit

code_to_test = """

class Solution:
    def reverse(self, x):
        if x < 2147483647 and x > -2147483648:
            s = ''
            if x < 0:
                s+= '-'
                x*=-1
            for i in range(len(str(x))-1,-1,-1):
                s = s + str(x)[i]
            return(int(s) if int(s) < 2147483647 and int(s) > -2147483648 else 0)
        else:
            return (0)

result = Solution()
x = 1534236469
print(result.reverse(x))
"""

elapsed_time = timeit.timeit(code_to_test, number=10)/10
print(elapsed_time)