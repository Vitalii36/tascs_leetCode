''' Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly
above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]


Constraints:

1 <= numRows <= 30 '''
import logging


class Solution:
    def generate(self, numRows):
        ls = []
        for i in range(numRows):
            if not ls:
                ls.append([i+1])
            elif len(ls) == 1:
                ls.append([i, i])
            else:
                f, c = [1, 1], ls[-1]
                while len(c) > 1:
                    g = sum(c[:2])
                    c = c[1:]
                    f.insert(len(f)-1, g)
                ls.append(f)
        return ls


result = Solution()
numRows = 5
print(result.generate(numRows))
