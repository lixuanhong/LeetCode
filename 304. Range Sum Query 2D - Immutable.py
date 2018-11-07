"""
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 ≤ row2 and col1 ≤ col2.
"""

"""
思路：因为需要多次search, 动态规划。Time Complexity: O(1)
"""

class NumMatrix(object):

    def __init__(self, matrix):

        if matrix == 0 or matrix == None:
            return None
        m, n = len(matrix), len(matrix[0])
        sum = [[0 for j in range(n+1)] for i in range(m+1)]  #避免边界问题，多加一行和一列

        for i in range(1, m+1):
            for j in range(1, n+1):
                sum[i][j] = matrix[i-1][j-1] + sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1]


    def sumRegion(self, row1, col1, row2, col2):

        return sum[row2+1][col2+1] - sum[row2+1][col1] - sum[row1][col2+1] + sum[row1][col1]


#Time Limit Exceed
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """

        r = len(matrix)
        c = len(matrix[0])
        if r == 0 or c == 0:
            return None
        self.m = [[0 for j in range(c)] for i in range(r)]

        for i in range(r):
            for j in range(c):
                self.m[i][j] = matrix[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        sum = 0
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                sum += self.m[i][j]
        return sum
