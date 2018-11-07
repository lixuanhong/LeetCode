"""
On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves. The rows and columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).

A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

The knight continues moving until it has made exactly K moves or has moved off the chessboard. Return the probability that the knight remains on the board after it has stopped moving.



Example:

Input: 3, 2, 0, 0
Output: 0.0625
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.


Note:

N will be between 1 and 25.
K will be between 0 and 100.
The knight always initially starts on the board.

"""

"""
思路：动态规划 Time Complexity: O(k*N^2) Space Complexity: O(N^2)
https://www.youtube.com/watch?v=MyJvMydR2G4
"""

class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        dp0 = [[0 for j in range(N)] for i in range(N)]
        dp0[r][c] = 1
        dirs = [[1, 2], [-1, -2], [1, -2], [-1, 2],
                [2, 1], [-2, -1], [2, -1], [-2, 1]]                   #8个方向的move
        for k in range(K):
            dp1 = [[0 for j in range(N)] for i in range(N)]
            for i in range(N):
                for j in range(N):
                    for dir in dirs:
                        x = i + dir[0]
                        y = j + dir[1]
                        if 0 <= x < N and 0 <= y < N:
                            dp1[x][y] += dp0[i][j]
            dp0 = dp1                                             #将dp0和dp1交换

        total = 0
        for i in range(N):
            for j in range(N):
                total += dp0[i][j]
        return total*1.0/8.0**K
