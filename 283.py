"""
Move Zeroes

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

"""

class Solution(object):
    def moveZeroes(self, nums):
        for n in nums:
            if n == 0:
                nums.remove(0)
                nums.append(0)
        return nums

obj = Solution()
nums = [0,1,0,3,12]
print(obj.moveZeroes(nums))
