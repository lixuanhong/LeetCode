"""
Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

Input:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

Output:

     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
"""


class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        r1, c1, c2 = len(A), len(A[0]), len(B[0])
        res = [[0 for j in range(c2)] for i in range(r1)]
        for i in range(r1):
            for j in range(c1):                         #思路：交换顺序，检查元素是否为0，如果为0就跳过！！
                if A[i][j] == 0:
                    continue
                for k in range(c2):
                    res[i][k] += A[i][j] * B[j][k]
        return res




# Brutal Force O(N^3) - Time Limit Exceed
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        r1, c1, c2 = len(A), len(A[0]), len(B[0])
        res = [[0 for j in range(c2)] for i in range(r1)]
        for i in range(r1):
            for j in range(c2):
                for k in range(c1):
                    res[i][j] += A[i][k] * B[k][j]
        return res
