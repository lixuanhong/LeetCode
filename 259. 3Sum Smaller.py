"""
Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

Example:

Input: nums = [-2,0,1,3], and target = 2
Output: 2
Explanation: Because there are two triplets which sums are less than 2:
             [-2,0,1]
             [-2,0,3]
Follow up: Could you solve it in O(n2) runtime?
"""

class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = 0
        if len(nums) <= 2: return res
        for i in range(len(nums) - 2):
            left, right = i+1, len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] < 2:
                    res += right - left          #相当于right往前到left+1的所有数都符合这个要求！！！
                    left += 1
                else:
                    right -= 1
        return res
