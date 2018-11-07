"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""


class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)         #这里是关键，nums是从0开始的连续整数缺一位
        sum = (0 + n) * (n + 1) / 2   #奇偶相乘一定是偶数
        for i in nums:
            sum -= i
        return sum
