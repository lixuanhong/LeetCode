"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
Each number in candidates may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""

class Solution(object):
    def combinationSum2(self, candidates, target):
        def dfs(candidates, target, s, cur, ans):
            if target == 0:
                if list(cur) not in ans:     #这道题和Combination Sum的区别在于input的数字有可能重复，但是在Combination Sum里面的input是not duplicate
                    ans.append(list(cur))
            for i in range(s, len(candidates)):
                if candidates[i] > target: break
                cur.append(candidates[i])
                dfs(candidates, target - candidates[i], i+1, cur, ans) #s取数从i+1之后开始，能够保证每个数字只取一次
                cur.pop()

        ans = []
        candidates.sort()
        dfs(candidates, target, 0, [], ans)
        return ans

obj = Solution()
candidates = [10,1,2,7,6,1,5]
target = 8
print(obj.combinationSum2(candidates, target))
