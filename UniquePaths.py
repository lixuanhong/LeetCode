"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
"""

# My Solution - 二维动态规划
class Solution(object):
    def uniquePaths(self, m, n):
        res = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            res[i][0] = 1
        for j in range(n):
            res[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                res[i][j] = res[i-1][j] + res[i][j-1]
        return res[m-1][n-1]


My Solution - 递归，超时！
class Solution(object):
    def uniquePaths(self, m, n):
        if m == 1 or n == 1: return 1
        if m == 2 and n == 2: return 2
        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)

obj = Solution()
print(obj.uniquePaths(23,12))
# print(obj.uniquePaths(7,3))
