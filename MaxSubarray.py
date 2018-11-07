"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

#动态规划 - 如果i前面元素之和是负数，那么新的序列从i开始往后加
class Solution:
    def maxSubArray(self, nums):
        res = nums[0]
        sum = nums[0]
        for i in range(1, len(nums)):
            sum = max(sum + nums[i], nums[i])
            if sum > res:
                res = sum
        return res


nums = [-2,1,-3,4,-1,2,1,-5,4]
obj = Solution()
print(obj.maxSubArray(nums))
