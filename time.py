import timeit

code_to_test = """

class Solution:
    def convert(self, s, numRows):
        result_list = []
        for j in range(numRows):
            letter_list,  num_list = [], []
            k = 0
            print(j, round(len(s)/(numRows-j+1)))
            for i in range(round(len(s)/(numRows-j+1))):
                letter_list.append(s[k:k+j+1])
                num_list.append(k)
                k+= numRows-j+1

            for i, n in enumerate(num_list):
                #print(n, i)
                #print(s[n+i:])
                s = s[:n-i]+s[n-i+1:]

            result_list.append(letter_list)
            print(letter_list, num_list, s)
        return (result_list)


result = Solution()
s = "PAYPALISHIRING"
num = 3
print(result.convert(s, num))
"""

elapsed_time = timeit.timeit(code_to_test, number=10)/10
print(elapsed_time)