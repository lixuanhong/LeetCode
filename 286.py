"""
Walls and Gates

You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example:

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
"""

class Solution(object):
    def wallsAndGates(self, rooms):
        if rooms == None or len(rooms) == 0: return

        # m = len(rooms)
        # n = len(rooms[0])

        for i in range(len(rooms)):                          #防止dfs里面没有全局变量出错
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    self.dfs(rooms, i, j, 0)

    def dfs(self, rooms, i, j, val):
        if i < 0 or j < 0 or i >= len(rooms) or j >= len(rooms[0]) or rooms[i][j] < val: return  #注意：这里是rooms[i][j] < val 如果是rooms[i][j] < 0会超时！！
        rooms[i][j] = val
        dfs(rooms, i+1, j, val+1)
        dfs(rooms, i-1, j, val+1)
        dfs(rooms, i, j+1, val+1)
        dfs(rooms, i, j-1, val+1)
