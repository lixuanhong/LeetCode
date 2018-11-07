"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.

"""
#思路：如果题目只要求计算数量而不要求提供解，通常情况下用动态规划dp；如果要求提供解，一般用dfs
#状态转移方程： dp[x+c] = min(dp[x]+1, dp[x+c]) 其中dp[x]代表凑齐金额x所需的最少硬币数，c为可用的硬币面值
#初始方程：dp[0] = 0  凑齐0块钱所需要的硬币数量是0
class Solution(object):
    def coinChange(self, coins, amount):
        dp = [0] + [-1] * amount
        for x in range(amount):
            if dp[x] < 0:
                continue
            for c in coins:
                if x + c > amount:
                    continue
                if dp[x+c] < 0 or dp[x+c] > dp[x]+1:
                    dp[x+c] = dp[x] + 1
        return dp[amount]

obj = Solution()
coins = [1,2,5]
amount = 11
print(obj.coinChange(coins, amount))






obj = Solution()
coins = [1,2,5]
amount = 11
print(obj.coinChange(coins, amount))
