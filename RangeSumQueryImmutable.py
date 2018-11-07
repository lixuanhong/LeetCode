"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
"""

"""
思路：一道很简单的动态规划题
sum[i] 用来存储 nums[0] + nums[1] + nums[2] + ...nums[i]
通过预处理来降维，每次查询的time complexity O(1)
"""

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        n = len(nums)
        if n == 0:
            return
        self.sums = [0] * n
        self.sums[0] = nums[0]
        for i in range(1, n):
            self.sums[i] = self.sum[i-1] + nums[i]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.sums[j]
        return self.sums[j] - self.sums[i-1]
