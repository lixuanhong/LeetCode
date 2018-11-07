"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""
#动态规划
class Solution:
    def maxProfit(self, prices):
       if len(prices) <= 1:
           return 0
       low = prices[0]
       maxprofit = 0
       for i in range(len(prices)):
           if prices[i] < low: low = prices[i]
           maxprofit = max(maxprofit, prices[i]-low)
       return maxprofit




# My Solution - Time Limit Exceed
class Solution:
    def maxProfit(self, prices):
        res = 0
        for i in range(len(prices)-1):
            for j in range(i, len(prices) - 1):
                if prices[j+1] < prices[i]:
                    continue
                profit = prices[j+1] - prices[i]
                res = max(res, profit)
        return res

obj = Solution()
prices = [7,6,4,3,1]
print(obj.maxProfit(prices))
