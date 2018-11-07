"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
"""

#思路：贪心解法 - 遍历数组，剩余步数step不为零的前提下，每次向前移动一步，将当前的num[i]和step相比较取较大者，作为剩余步数step。
class Solution(object):
    def canJump(self, nums):
        step = nums[0]
        for i in range(1, len(nums)): #如果len(nums) <=1, 那么直接return True
            if step > 0:
                step -= 1
                step = max(step, nums[i])
            else:
                return False
        return True #如果走完循环，剩余step大于等于0，那么就能到达




obj = Solution()
nums = [2,3,1,1,4]
print(obj.canJump(nums))
