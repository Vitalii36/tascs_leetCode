'''Given an integer rowIndex, return the rowIndexth (0-indexed) row of
the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly
 above it as shown

 Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
'''


class Solution:
    def getRow(self, rowIndex):
        ls = []
        for i in range(rowIndex+1):
            if not ls:
                ls = [i + 1]
            elif len(ls) == 1:
                ls = [i, i]
            else:
                f, c = [1, 1], ls
                while len(c) > 1:
                    g = sum(c[:2])
                    c = c[1:]
                    f.insert(len(f) - 1, g)
                ls = f
        return ls

result = Solution()
rowIndex = 3
print(result.getRow(rowIndex))

