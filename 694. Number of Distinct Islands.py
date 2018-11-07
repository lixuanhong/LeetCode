"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Example 1:
11000
11000
00011
00011
Given the above grid map, return 1.
Example 2:
11011
10000
00001
11011
Given the above grid map, return 3.

Notice that:
11
1
and
 1
11
are considered different island shapes, because we do not consider reflection / rotation.
Note: The length of each dimension in the given grid does not exceed 50.
"""

"""
思路：这道题让我们求不同岛屿的个数，是之前那道Number of Islands的拓展，这道题的难点是如何去判断两个岛屿是否是不同的岛屿，首先1的个数肯定是要相同，但是1的个数相同不能保证一定是相同的岛屿，
比如例子2中的那两个岛屿的就不相同，就是说两个相同的岛屿通过平移可以完全重合，但是不能旋转。那么我们如何来判断呢，我们发现可以通过相对位置坐标来判断，比如我们使用岛屿的最左上角的1当作基点，
那么基点左边的点就是(0,-1)，右边的点就是(0,1), 上边的点就是(-1,0)，下面的点就是(1,0)。那么例子1中的两个岛屿都可以表示为[(0,0), (0,1), (1,0), (1,1)]，点的顺序是基点-右边点-下边点-右下点。
通过这样就可以判断两个岛屿是否相同了。直接将相对坐标存入数组中，然后把整个数组放到集合set中，还是会去掉相同的数组，而且这种解法直接在grid数组上标记访问过的位置。
"""

class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dirs = {(0,-1), (-1, 0), (0, 1), (1, 0)}
        m, n = len(grid), len(grid[0])
        res = set()

        def dfs(grid, x0, y0, i, j, v):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] <= 0:
                return
            grid[i][j] *= -1
            v.append((i - x0, j - y0))
            for dir in dirs:
                dfs(grid, x0, y0, i + dir[0], j + dir[1], v)

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1: continue
                v = []
                dfs(grid, i, j, i, j, v)
                res.add(tuple(v))           #注意：这里res是个set, 需要用add; 另外set不能add list, 需要把list转换成为tuple
        return len(res)
