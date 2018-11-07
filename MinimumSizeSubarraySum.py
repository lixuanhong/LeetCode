""" Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s.
If there isn't one, return 0 instead.

Example:

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

"""
# O(n) 思路：前向双指针。快针定位到大于等于目标值子序列的最后一个元素，慢针再逼近到刚好小于目标值子序列的第一个元素。
def minSubArrayLen(s, nums):
    n = len(nums)
    if n == 0: return 0
    left = right = total = 0
    res = n+1
    while right < n:
        while right < n and total < s:
            total += nums[right]
            right += 1
        while left < right and total >= s: #shrink the sliding window size
            res = min(res, right - left)
            total -= nums[left]
            left += 1
    return res if res<=n else 0

# Simplified version
class Solution:
    def minSubArrayLen(self, s, nums):
        left, res, total = 0, len(nums) + 1, 0
        for right, num in enumerate(nums):
            total += num
            while total >= s:
                res = min(res, right - left + 1)
                total -= nums[left]
                left += 1
        return res if res <=n else 0


# O(nlogn) - bineary search
class Solution:
    def minSubArrayLen(self, s, nums):
        left = 0
        res = len(nums) + 1

        for i in range(1, len(nums)):
            nums[i] += nums[i-1]

        for right, n in enumerate(nums):
            if n >= s:
                left = self.leftMost(left, right, nums, s, n)
                res = min(res, right - left + 1)

        return res if res <= len(nums) else 0

    def leftMost(self, left, right, nums, s, n):
        while left < right:
            mid = left + (right - left) // 2

            if n - nums[mid] >= s:
                left = mid + 1
            else:
                right = mid

        return left
