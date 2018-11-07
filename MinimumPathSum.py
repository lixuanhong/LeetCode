"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""

class Solution(object):
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        res = [[0 for j in range(n)] for i in range(m)]
        res[0][0] = grid[0][0]
        for i in range(1, m):
            res[i][0] = res[i-1][0] + grid[i][0]

        for j in range(1, n):
            res[0][j] = res[0][j-1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                res[i][j] = min(res[i-1][j], res[i][j-1]) + grid[i][j]

        return res[m-1][n-1]

obj = Solution()
grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
print(obj.minPathSum(grid))
