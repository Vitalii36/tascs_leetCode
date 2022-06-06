"""
Given an array of points on the X-Y plane points where points[i] = [xi, yi], return the area of the largest triangle
that can be formed by any three different points. Answers within 10-5 of the actual answer will be accepted.


Example 1:


Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2.00000
Explanation: The five points are shown in the above figure. The red triangle is the largest.
Example 2:

Input: points = [[1,0],[0,0],[0,1]]
Output: 0.50000


Constraints:

3 <= points.length <= 50
-50 <= xi, yi <= 50
All the given points are unique.
"""


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def get_area(x, y):
            area = 0.5 * ((x[0] * (y[1] - y[2])) + (x[1] * (y[2] - y[0])) + (x[2] * (y[0] - y[1])))
            return area

        import itertools
        square_traingular = -1
        for obj in itertools.product(points, repeat=3):
            area = get_area([obj[0][0], obj[1][0], obj[2][0]], [obj[0][1], obj[1][1], obj[2][1]])
            if area > square_traingular:
                square_traingular = area
        return square_traingular
