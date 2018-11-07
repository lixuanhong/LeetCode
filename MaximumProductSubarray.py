"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

"""
思路：动态规划，主要需要考虑负负得正这种情况，比如之前的最小值是一个负数，再乘以一个负数就有可能成为一个很大的正数。
时间复杂度O（N）
"""


class Solution(object):
    def maxProduct(self, nums)：
        if len(nums) == 0:
            return 0
        min_tmp = nums[0]
        max_tmp = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            a = nums[i] * min_tmp
            b = nums[i] * max_tmp
            c = nums[i]
            min_tmp = min(min(a,b),c)
            max_tmp = max(max(a,b),c)
            result = max_tmp if max_tmp > result else result
        return result




#My Solution - Time Limit Exceeded
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        max_product = float("-inf")
        for i in range(len(nums)):
            product = nums[i]
            max_product = max(product, max_product)
            for j in range(i+1, len(nums)):
                product = product * nums[j]
                max_product = max(product, max_product)
        return max_product
