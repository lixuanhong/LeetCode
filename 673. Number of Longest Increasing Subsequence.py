"""
Given an unsorted array of integers, find the number of longest increasing subsequence.

Example 1:
Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:
Input: [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.
Note: Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int.
"""

"""
思路：和最长递增子序列不同的是，最优解可能不止一个，这种情况会发生在 dp[i] == dp[j]+1，即i与j具有相同的序列长度，那么我们更新当前长度ct[i] = ct[i]+ct[j]
若dp[j]+1>dp[i],则更新最长子序列的个数为dp[j]的个数
"""

class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 or nums is None:
            return 0
        n = len(nums)
        dp = [1] * n
        ct = [1] * n
        for i in range(n):
            for j in range(i):
                if num[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    ct[i] = ct[j]
                elif nums[i] > nums[j] and dp[i] == dp[j] + 1:
                    ct[i] += ct[j]
        max_length = max(dp)

        res = 0
        for i in range(len(ct)):
            if dp[i] == max_length:
                res += ct[i]
        return res
