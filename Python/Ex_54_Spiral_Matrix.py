"""
Given an m x n matrix, return all elements of the matrix in spiral order.



Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        cm = []
        while matrix and matrix[0]:
            cm.extend(matrix[0])
            matrix = matrix[1:]
            l_m = len(matrix)
            el = []
            if l_m > 1:
                for o in range(0, l_m - 1):
                    if len(matrix[o]) == 1:
                        cm.extend([i[0] for i in matrix[:-1]])
                        matrix = [matrix[-1]]
                        break
                    cm.append(matrix[o][-1])
                    el.append(matrix[o][0])
                    matrix[o] = matrix[o][1:-1]

            if l_m:
                g = matrix[-1]
                g.reverse()
                el.reverse()
                matrix = matrix[:-1]
                cm.extend(g)
                cm.extend(el)
        return cm
