"""
You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

Note: You can assume that

0 <= amount <= 5000
1 <= coin <= 5000
the number of coins is less than 500
the answer is guaranteed to fit into signed 32-bit integer


Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1


Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.


Example 3:

Input: amount = 10, coins = [10]
Output: 1
"""

"""
思路：建议和这一道题leetcode 322. Coin Change 类似背包问题 一起学习

还有这一道题leetcode 377. Combination Sum IV 组合之和 + DP动态规划 + DFS深度优先遍历一起学习

这两到的DP的出发点是不一样的，322是尽量凑够amout，然后求解最小的数量，本题则是求解能够组成amount的所有的情况的计数，所以这两道题很类似，但是不一样

还建议和leetcode 279. Perfect Squares 类似背包问题 + 很简单的动态规划DP解决 一起学习

还有leetcode 474. Ones and Zeroes若干0和1组成字符串最大数量+动态规划DP+背包问题

"""

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0] * (amount + 1)   #表示组成钱数i的不同方法
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]
        return dp[amount]
