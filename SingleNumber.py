"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""

# 另外一种思路：异或操作 x^0 = x; x^x=0
class Solution:
    def singleNumber(self, nums):
        ans = nums[0]
        for i in range(1, len(nums)):
            ans = ans ^ nums[i]
        return ans


import collections
class Solution:
    def singleNumber(self, nums):
        dict = collections.Counter(nums)
        for item in dict:
            if dict[item] == 1:
                return item


class Solution:
    def singleNumber(self, nums):
        dict = {}
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]] = 1
            else:
                dict[nums[i]] += 1

        for item in dict:
            if dict[item] == 1:
                return item


obj = Solution()
nums = [4,1,2,1,2]
print(obj.singleNumber(nums))
