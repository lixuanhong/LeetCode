"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

"""

"""
思路：https://www.youtube.com/watch?v=mKXIH9GnhgU
这道题和continuous subarray sum思路相似！
"""

class Solution(object):
    def subarraySum(self, nums, k):
        sum, res = 0, 0
        dict = collections.defaultdict(int)   #这里一定要表明数据类型(因为已经初始化，便于不在字典里面的时候可以直接++)
        dict[0] = 1                           #当sum == k的时候，sum - k = 0, 需要加上这种情况
        for i in range(len(nums)):
            sum += nums[i]
            if sum - k in dict:               #必须是sum - k，因为sum是累加的，如果字典里面存在sum - k, 那么sum - (sum - k)就符合要求了！！
                res += dict[sum-k]
            dict[sum] += 1                    #本身默认值是0
        return res
