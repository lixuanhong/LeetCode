"""
Pain House

There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:

Input: [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
             Minimum cost: 2 + 5 + 3 = 10.

"""

"""
思路：一道很明显的动态规划的题目. 每个房子有三种染色方案, 那么如果当前房子染红色的话, 最小代价将是上一个房子的绿色和蓝色的最小代价+当前房子染红色的代价.
对另外两种颜色也是如此. 因此动态转移方程为:

dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0];

dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1];

dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2];

Time: O(N)
Space: O(1)

"""

class Solution(object):
    def minCost(self, costs):
        if costs == None or len(costs) == 0:
            return 0
        dp = [[0 for i in range(3)] for j in range(len(costs))]
        dp[0][0] = costs[0][0]
        dp[0][1] = costs[0][1]
        dp[0][2] = costs[0][2]

        for i in range(1, len(costs)):
            dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
            dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
            dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]

        return min(dp[len(costs)-1][0], dp[len(costs)-1][1], dp[len(costs)-1][2])

obj = Solution()
costs = [[17,2,17],[16,16,5],[14,3,19]]
print(obj.minCost(costs))
