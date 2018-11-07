"""
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5
Explanation:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
"""

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        n = len(nums)
        dp = [collections.defaultdict(int) for i in range(n+1)]   #注意：不能使用[collections.defaultdict(int) * (n+1)]! dp是由defaultdict组成的list,
                                                                  #每一个defaultdict都是一个字典，可以存储由i个元素组成的所有和的(key, value)
        dp[0][0] = 1                                       #第一个下标表示用的元素数量，第二个下标表示sum值, 也就是字典的key
        for i, num in enumerate(nums):
            for sum, cnt in dp[i].items():
                dp[i+1][sum + num] += cnt                 #i是index, 元素数量是index+1
                dp[i+1][sum - num] += cnt
        return dp[n][S]
