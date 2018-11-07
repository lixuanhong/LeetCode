"""
Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:

Input: nums = [1, -1, 5, -2, 3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
Example 2:

Input: nums = [-2, -1, 2, 1], k = 1
Output: 2
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
Follow Up:
Can you do it in O(n) time?

"""


class Solution(object):
    def maxSubArrayLen(self, nums, k):
        sum, res = 0, 0
        dict = {}
        for i in range(len(nums)):
            sum += nums[i]
            if sum == k:
                res = max(res, i + 1)

            diff = sum - k
            if diff in dict:                      #注意：这里直接在dict里面查找，如果写成dict.keys()是生成一个数组，然后在数组里面查找，降低速度不能AC
                res = max(res, i - dict.get(diff))
            if sum not in dict:
                dict[sum] = i
        return res
