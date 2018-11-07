"""
Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to the multiple of k, that is, sums up to n*k where n is also an integer.

Example 1:
Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:
Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
Note:
The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.
"""

#思路：若数字a和b分别除以数字c，若得到的余数相同，那么(a-b)必定能够整除c；建立余数和当前位置之间的映射
#O(N)
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict = {0:-1}                     #初始化很重要
        sum = 0
        for idx, num in enumerate(nums):
            sum += num
            m = sum % k if k else sum
            if m not in dict:
                dict[m] = idx
            elif dict[m] + 1 < i:       #保证至少连续两位数的和！
                return True
        return False


#这个方法可以通过，但是时间复杂度为O(N^2)
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        for i in range(len(nums)):
            sum = nums[i]
            for j in range(i+1, len(nums)):
                sum += nums[j]
                if sum == k:
                    return True               # 注意：sum = k = 0是True !!
                if k!= 0 and sum % k == 0:
                    return True
        return False
