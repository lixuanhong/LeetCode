"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
"""

class Solution(object):
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        for index, value in enumerate(nums):
            if target <= value:
                return 0
            if index < len(nums) - 1: #这里要注意index+1 out of list range的问题
                if target > value and target <= nums[index+1]:
                    return index + 1
            if index == len(nums) - 1 and target > value:
                return index+1

obj = Solution()
print(obj.searchInsert([1,3,5,6], 0))
