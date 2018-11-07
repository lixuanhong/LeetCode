"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

#My Solution
class Solution(object):
    def permute(self, nums):
        n = len(nums)
        if n == 0:
            return []
        cur, res = [], []
        self.dfs(nums, 0, cur, res)
        return res

    def dfs(self, nums, k, cur, res):
        if k == len(nums):
            res.append(list(cur))
            return

        for i in range(len(nums)):
            if nums[i] in cur:                 #因为数组里面的值都是distinct, 所以可以简单判断某个元素是否已经取过
                continue
            cur.append(nums[i])
            self.dfs(nums, k+1, cur, res)
            cur.pop()




class Solution:
    def permute(self, nums):

        def helper(nums, tmp, ans):
            if len(nums) == 0: return []
            if len(tmp) == len(nums):
                ans.append(list(tmp))

            for i in range(len(nums)):
                if nums[i] in tmp:           #因为数组里面的值都是distinct, 所以可以简单判断某个元素是否已经取过
                    continue
                tmp.append(nums[i])
                helper(nums, tmp, ans)
                tmp.pop()

        ans = []
        helper(nums, [], ans)
        return ans
