"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

class Solution(object):
    def subsets(self, nums):
        def dfs(nums, tmp, k, s, res):
            if len(tmp) == k:
                res.append(list(tmp))
            for i in range(s, len(nums)):
                tmp.append(nums[i])
                dfs(nums, tmp, k, i+1, res)
                tmp.pop()
            return res

        ans = [[]]
        if len(nums) == 0: return ans
        for k in range(1, len(nums)):
            res = []
            dfs(nums, [], k, 0, res)
            ans.extend(res)
        ans.append(nums)
        return ans

obj = Solution()
print(obj.subsets([1,2,3]))
