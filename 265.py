"""
Paint House II

There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:

Input: [[1,5,3],[2,9,4]]
Output: 5
Explanation: Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5;
             Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5.
Follow up:
Could you solve it in O(nk) runtime?

"""

"""
这道题是之前那道Paint House的拓展，那道题只让用红绿蓝三种颜色来粉刷房子，而这道题让我们用k种颜色，这道题不能用之前那题的解法，会TLE。
这题的解法的思路还是用DP，但是在找不同颜色的最小值不是遍历所有不同颜色，而是用min1和min2来记录之前房子的最小和第二小的花费的颜色，
如果当前房子颜色和min1相同，那么我们用min2对应的值计算，反之我们用min1对应的值，这种解法实际上也包含了求次小值的方法.
"""


class Solution(object):
    def minCostII(self, costs):
        if costs == None or len(costs) == 0:
            return 0

        n = len(costs) #number of houses
        k = len(costs[0]) #color choices

        dp = [[0 for i in range(k)] for j in range(n)]

        preLeast, preSecond, preIndex = 0, 0, -1
        for i in range(n):
            curLeast, curSecond, curIndex = float("inf"), float("inf"), -1   #float("inf") represents infinity
            for j in range(k):
                if j == preIndex:
                    dp[i][j] = costs[i][j] + preSecond
                else:
                    dp[i][j] = costs[i][j] + preLeast

                #更新最小值，次小值，最小值index
                if (dp[i][j] < curLeast):
                    curSecond = curLeast
                    curLeast = dp[i][j]
                    curIndex = j
                elif (dp[i][j] < curSecond):
                    curSecond = dp[i][j]

            preLeast = curLeast
            preSecond = curSecond
            preIndex = curIndex

        return preLeast
