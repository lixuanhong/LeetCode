"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

#My Solution - still DP
class Solution:
    def maxProfit(self, prices):
        if len(prices) == 0 or not prices:
            return 0
        dp = [0] * len(prices)
        min = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < min:
                min = prices[i]
                dp[i] = dp[i-1]
            elif prices[i] > prices[i-1]:
                dp[i] = max(prices[i] - prices[i-1] + dp[i-1], prices[i] - min)
            else:
                dp[i] = dp[i-1]
        return max(dp)





# Better Solution - 贪心算法
class Solution:
    def maxProfit(self, prices):
        maxprofit = 0
        for i in range(1, len(prices)):
            if prices[i] >= prices[i-1]:
                maxprofit += prices[i] - prices[i-1]
        return maxprofit

"""
按照对题目的理解，对于类似[1,2,3,0]这样的序列，最正确的做法是“1元买入3元卖出”。而上面的解法感觉像是“1元买入2元卖出，2元买入3元卖出”，当然，结果是对的，而且其实上面的解法相当于代码优化。比较繁一点的解法是“先找局部最小，再找局部最大”这样的循环
"""

# 另外一种解法
class Solution:
    def maxProfit(self, prices):
        res = 0
        i = 0
        while i < len(prices):
            while i < len(prices)-1 and prices[i+1] <= prices[i]:
                i += 1    #找最小的价格
            j = i + 1     #j对应的价格肯定大于i
            while j < len(prices)-1 and prices[j+1] >= prices[j]:
                j += 1   #找最大价格j
            res += prices[j] - prices[i] if j < len(prices) else 0
            i = j + 1
        return res




# My Solution
class Solution:
    def maxProfit(self, prices):
        if len(prices) <= 1: return 0
        low = prices[0]
        res = 0
        for i in range(1, len(prices)):
            maxprofit = 0
            if prices[i] <= low:
                low = prices[i]
            elif prices[i] > low and i == len(prices) - 1:
                return res + prices[i] - low
            elif prices[i] > low and prices[i+1] > prices[i]:
                if i == len(prices) - 2:
                    return res + prices[i+1] - low
                else:
                    continue
            elif prices[i] > low and prices[i+1] < prices[i]:
                maxprofit = prices[i] - low
                res += maxprofit
                low = prices[i+1]
        return res

obj = Solution()
prices = [1,2,3,4,5]
print(obj.maxProfit(prices))
