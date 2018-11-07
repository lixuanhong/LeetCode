"""
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

n = 3
root: 1 left: 0 right: 2 f(0) * f(2)
root: 2 left: 1 right: 1 f(1) * f(1)
root: 3 left: 2 right: 0 f(2) * f(0)

f(n) = f(0)*f(n-1) + f(1)*f(n-2) + ... + f(n-2)*f(1) + f(n-1)*f(0)
"""

"""
解题思路：这题从数学上讲，其实是卡特兰数。不过我们显然不从数学上来解决这个问题。这题是求二叉树的棵数。这里有个解题技巧：一般来说求数量，要首先想到使用动态规划（dp），
而如果是像下一题的要求，不只是数量，还要把所有的树都枚举出来，就要使用dfs（深度优先搜索）来遍历决策树了。

那么这道题是使用动态规划来解决的。那么如何去求这个问题的状态转移方程呢？其实大部分动态规划的难点都是求状态转移方程。n=0时，为空树，那么dp[0]=1; n=1时，
显然也是1，dp[1]=1；n=2时，dp[2]=2; 对于n>2时，dp[n]=dp[0]*dp[n-1]+dp[1]*dp[n-2]+......+dp[n-1]*dp[0]；这不就是卡特兰数的定义吗？编程很容易实现。
"""


class Solution(object):
    def numTrees(self, n):
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                dp[i] += dp[j] * dp[i-j-1] #要扣除root那位
        return dp[n]
