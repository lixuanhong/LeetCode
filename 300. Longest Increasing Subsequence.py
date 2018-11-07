"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""
“”“
思路：dp[i] 为 以 A[i]结尾的LIS，那么对于dp[i]有dp[i] =max( dp[j] + 1) [0<= j < i, nums[j] < nums[i]]

效率为O(n^2)

”“”

class Solution(object):
    def lengthOfLIS(self, nums):
        if not nums or len(nums) == 0: return 0

        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)
