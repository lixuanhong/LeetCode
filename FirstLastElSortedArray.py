"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

"""
class Solution(object):
    def searchRange(self, nums, target):
        left = 0
        right = len(nums) - 1
        start = end = 0
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                start = end = mid
                while start>= 1 and nums[start-1] == target: #注意：index不能out of range
                    start -= 1
                while end<= len(nums)-2 and nums[end+1] == target: #注意：index不能out of range
                    end += 1
                return [start, end]
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return [-1, -1]

obj = Solution()
nums = [5,7,7,8,8,10]
print(obj.searchRange(nums, 8))
