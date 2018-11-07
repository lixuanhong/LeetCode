"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""

class Solution(object):
    def combine(self, n, k):
        def dfs(arr, tmp, k, s, res):
            if len(tmp) == k:
                res.append(list(tmp))
            for i in range(s, len(arr)):
                tmp.append(arr[i])
                dfs(arr, tmp, k, i+1, res)
                tmp.pop()

        arr = [i+1 for i in range(n)]
        res = []
        dfs(arr, [], k, 0, res)
        return res

obj = Solution()
print(obj.combine(4, 2))
