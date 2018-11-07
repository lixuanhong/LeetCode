"""
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
"""

"""
思路：一个背包的题目，背包容量为数组中元素和的一半＋１，这样只要看是否有元素可以正好填满背包即可．但是每个元素只能用一次，
所以在尝试放一个元素的时候还要避免他对尝试放其他位置时对自己的影响．所以在尝试放一个元素到背包的时候需要从容量最大的位置开始，
如果（当前位置－当前元素大小）位置可以通过放置之前的元素达到，则当前位置也可以通过放置当前元素正好达到这个位置．
状态转移方程为：dp[i] = dp[i] || dp[i - nums[k]];

https://blog.csdn.net/qq508618087/article/details/52774116?utm_source=copy
"""


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum = 0
        for num in nums:
            sum += num
        if sum % 2 != 0:
            return False
        dp = [0] * (sum/2 + 1)
        dp[0] = 1
        for i in range(len(nums)):
            for j in range(sum/2, nums[i]-1, -1):   #注意：这里是倒序，所以范围是nums[i]-1，能到nums[i]
                dp[j] = dp[j] or dp[j - nums[i]]
        return dp[sum/2] == 1
