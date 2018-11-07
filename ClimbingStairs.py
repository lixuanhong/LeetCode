"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""
#动态规划解法
class Solution(object):
    def climbStairs(self, n):
        if n == 1:        #必须加这个条件，否则后面dp[2]会出现index out of range的错误
            return 1
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        for x in range(3, n+1):
            dp[x] = dp[x-1] + dp[x-2]
        return dp[n]

#递归解法 
# class Solution(object):
#     def climbStairs(self, n):
#         if n == 1:
#             return 1
#         if n == 2:
#             return 2
#         res = 0
#         res += self.climbStairs(n-1) + self.climbStairs(n-2)
#         return res

obj = Solution()
print(obj.climbStairs(1))
