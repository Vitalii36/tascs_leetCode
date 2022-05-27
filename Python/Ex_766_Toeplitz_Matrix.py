"""
Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.



Example 1:


Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
Example 2:


Input: matrix = [[1,2],[2,2]]
Output: false
Explanation:
The diagonal "[1, 2]" has different elements.


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 20
0 <= matrix[i][j] <= 99
"""


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        if n == 1 or m == 1:
            return True
        v = n - 1
        h = 1
        while h != m - 1 or v != -1:
            a = v
            b = h
            num = -1
            while b != -1 and a != -1:
                if num == -1:
                    num = matrix[a][b]
                elif num != matrix[a][b]:
                    return False
                b -= 1
                a -= 1
            if h == m - 1:
                v -= 1
            else:
                h += 1
        return True
