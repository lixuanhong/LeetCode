"""
Number of Islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3

"""

"""
This is a variation of the standard problem: “Counting the number of connected components in an undirected graph”.
The problem can be easily solved by applying DFS() on each component. In each DFS() call, a component or a sub-graph is visited.
We will call DFS on the next un-visited component.
我们对每个有“1”的位置进行dfs，把和它四联通的位置全部变成“0”，这样就能把一个点推广到一个岛。
所以，我们总的进行了dfs的次数，就是总过有多少个岛的数目。
https://www.youtube.com/watch?v=RHUSlUevd8k
"""

class Solution(object):
    def numIslands(self, grid):
        if len(grid) == 0 or grid == None:
            return 0                             #所有题目第一步，确定边界条件

        res = 0
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':     #一定要注意等于符号是==，很容易犯错
                    self.dfs(grid, i, j)
                    res += 1
        return res

    def dfs(self, grid, i, j):
        m, n = len(grid), len(grid[0])          #前面的m, n是local变量
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == '0':    #grid[i][j] == '0'这个边界条件容易忽略
            return
        grid[i][j] = '0'
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
