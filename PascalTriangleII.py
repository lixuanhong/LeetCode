"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.
"""

class Solution:
    def getRow(self, rowIndex):
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1, 1]
        pre = self.getRow(rowIndex - 1)
        res = [1]
        for i in range(len(pre) - 1):
            res.append(pre[i] + pre[i+1])
        res.append(1)
        return res

obj = Solution()
print(obj.getRow(3))
