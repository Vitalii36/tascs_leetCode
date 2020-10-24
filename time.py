import timeit

code_to_test = """


result = Solution()
x = 1534236469
print(result.reverse(x))
"""

elapsed_time = timeit.timeit(code_to_test, number=10)/10
print(elapsed_time)