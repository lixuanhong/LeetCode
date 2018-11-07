"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""

#思路： 二分法，先判断中值是属于哪边的升序序列，再根据端点值继续判断 target 该落在左边还是右边区域
class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:              #这里需要注意的是left和right可以相等
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]:  #当nums[mid]属于左边升序序列 必须包括大于等于！！
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] <= nums[right]: #当nums[mid]属于右边升序序列 包括等于，没有风险！！
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
