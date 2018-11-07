"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

"""

class Solution(object):
    def subsetsWithDup(self, nums):
        def dfs(nums, tmp, k, s, res):
            if len(tmp) == k:
                if tmp not in res:
                    res.append(list(tmp))
            for i in range(s, len(nums)):
                tmp.append(nums[i])
                dfs(nums, tmp, k, i+1, res)
                tmp.pop()
            return res

        ans = [[]]
        nums.sort()
        if len(nums) == 0: return ans
        for k in range(1, len(nums)):
            res = []
            dfs(nums, [], k, 0, res)
            ans.extend(res)
        ans.append(nums)
        return ans

obj = Solution()
nums = [1, 2, 2]
print(obj.subsetsWithDup(nums))
