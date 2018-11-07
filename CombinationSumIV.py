"""
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?

"""

"""
dp([1,2,3],4) #  笛卡尔积
=U({1} * dp([1,2,3], 4-1), #{1,1,1,1}, {1,1,2}
   {2} * dp([1,2,3], 4-2), #{2,1,1}, {2,2}
   {3} * dp([1,2,3], 4-3)) #{3,1}

dp([1,2,3],3)
=U({1} * dp([1,2,3], 3-1), #{1,1,1}, {1,2}
   {2} * dp([1,2,3], 3-2), #{2,1}
   {3} * dp([1,2,3], 3-3)) #{3}

dp([1,2,3],2)
=U({1} * dp([1,2,3], 2-1),  #{1,1}
   {2} * dp([1,2,3], 2-2)） #{2}

dp([1,2,3],1)
=U({1} * dp([1,2,3], 1-1),  #{1}

dp([1,2,3], 0) = {} 只有一种解
"""

#思路：动态规划 Time Complexity O(target*|nums|) 52ms
# class Solution(object):
#     def combinationSum4(self, nums, target):
#         if nums == []:
#             return 0
#
#         dp = [0] * (target + 1) #memoization
#         dp[0] = 1 #构成结果0只有一种解{}
#
#         for i in range(1, target+1):
#             for x in nums:
#                 if x <= i:
#                     dp[i] += dp[i-x] #得到的是返回解得数量，遍历所有数字，所有子问题解的和就是新问题解的数量
#
#         return dp[target]
#
# obj = Solution()
# nums = [4, 2, 1]
# target = 32
# print(obj.combinationSum4(nums, target))


# 思路：recursion with meoization Time Complexity: O(sum{target/nums[i]}) Space Complexity: O(target) 没有通过Leetcode, Time Limited
class Solution(object):
    def combinationSum4(self, nums, target):
        def dp(nums, target):
            if target < 0: return 0
            if (memo[target] != 0):
                return memo[target]
            ans = 0
            for num in nums:
                ans += dp(nums, target - num)
            memo[target] = ans
            return memo[target]

        memo = [0] * (target + 1)
        memo[0] = 1
        return dp(nums, target)

obj = Solution()
nums = [4, 2, 1]
target = 32
print(obj.combinationSum4(nums, target))



# My Solution - Time Limited Not Work 错误原因：对题目理解有偏差，不是要求解，而是要求解得数量，用动态规划方法recursion with memoization
# class Solution:
#     def combinationSum4(self, nums, target):
#         def dfs(nums, target, cur, ans):
#             if target == 0:
#                 ans.append(list(cur))
#             for i in range(len(nums)): #这道题和前面的差异在于s=0,每一次都从头开始取值，因为顺序不同得到的数组结果算作是不同的结果, 这是一道排列题
#                 if nums[i] > target: break
#                 cur.append(nums[i])
#                 dfs(nums, target - nums[i], cur, ans)
#                 cur.pop()
#
#         ans = []
#         nums.sort()
#         dfs(nums, target, [], ans)
#         return ans
