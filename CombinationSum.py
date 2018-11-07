"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""
class Solution(object):
    def combinationSum(self,candidates, target):
        def dfs(candidates, target, s, cur, ans):
            if target == 0:
                return ans.append(list(cur)) #list(cur)是cur的一个copy,如果直接append cur, 后面当运行cur.pop()时，ans也会被pop掉

            for i in range(s, len(candidates)):        #backtracking method//choose/explore/unchoose
                if candidates[i] > target:
                    break
                cur.append(candidates[i]) #choose
                dfs(candidates, target - candidates[i], i, cur, ans) # explore
                cur.pop() #unchange - remove the last item; the list also changed

        ans = []
        candidates.sort()
        dfs(candidates, target, 0, [], ans) #不能直接return dfs, 因为dfs是动态递归的函数，结果随时在变化
        return ans


obj = Solution()
candidates = [2,3,6,7]
target = 7
print(obj.combinationSum(candidates, target))

"""
a = []
b = [2,2,3]
c = [7]
a.append(list(b))  ## append, pop等都是对list的操作，在这些操作之后，原来的list值被改变了; 这里list(b)是建立一个b的copy
a.append(c)
b.pop()  ==> 3
print(b) ==> [2,2]
print(a) ==> [[2,2,3],[7]]

"""
