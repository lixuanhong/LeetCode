"""
Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

Example:

Input: nums = [3,5,2,1,6,4]
Output: One possible answer is [3,5,1,6,2,4]

"""

"""
思路：跟Wiggle Sort II相比起来，这道题的条件宽松很多，只因为多了一个等号。由于等号的存在，当数组中有重复数字存在的情况时，也很容易满足题目的要求。
这道题我们先来看一种时间复杂度为O(nlgn)的方法，思路是先给数组排个序，然后我们只要每次把第三个数和第二个数调换个位置，第五个数和第四个数调换个位置，
以此类推直至数组末尾，这样我们就能完成摆动排序了。
"""

class Solution(object):
    def wiggleSort(self, nums):
        nums.sort()
        if len(nums) <= 2: return
        for i in range(2, len(nums), 2):
            nums[i], nums[i-1] = nums[i-1], nums[i]
