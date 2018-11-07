"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)


"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if len(nums) <= 1: return nums
        res = [1] * len(nums)
        left, right = 1, 1
        for i in range(1, len(nums)):
            left = nums[i-1] * left
            res[i] = left

        for i in range(len(nums) - 2, -1, -1):   #注意：中间-1表示到0，最后-1表示顺序减少1
             right = nums[i+1] * right
             res[i] *= right
        return res
