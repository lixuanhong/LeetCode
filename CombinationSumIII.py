"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:
All numbers will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""

class Solution:
    def combinationSum3(self, k, n):
        def dfs(k, n, s, cur, ans):
            candidates = [1,2,3,4,5,6,7,8,9]
            if n == 0 and k == 0: #这道题和CombinationSum II相比，多考虑一个结果数组长度k, 即递归深度
                if list(cur) not in ans:
                    ans.append(list(cur))
            for i in range(s,9):
                if candidates[i] > n: break
                cur.append(candidates[i])
                dfs(k-1, n-candidates[i], i+1, cur, ans) #每取值一次递归深度减1，直到找到目标值并且递归深度等于k
                cur.pop()

        ans = []
        dfs(k, n, 0, [], ans)
        return ans

obj = Solution()
print(obj.combinationSum3(3, 7))
print(obj.combinationSum3(3, 9))
