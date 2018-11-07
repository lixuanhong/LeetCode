"""
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

"""

class Solution(object):
    def generateMatrix(self, n):
        res = [[0 for i in range(n)] for j in range(n)] #很重要！！！不能写成[[0] * n] * n 否则复制给其中任何一个元素时，会导致其他元素随之而变化
        left = up = 0
        right = down = n - 1
        direct = 0 # 0 - go right 1 - go down 2 - go left 3 - go up
        j = 1
        while True:
            if direct == 0:
                for i in range(left, right+1):
                    res[up][i] = j
                    j += 1
                up += 1
            if direct == 1:
                for i in range(up, down+1):
                    res[i][right] = j
                    j += 1
                right -= 1
            if direct == 2:
                for i in range(right, left-1, -1):
                    res[down][i] = j     #在书写时要注意哪些是变化的，哪些是不变的，很容易把行列弄反
                    j += 1
                down -= 1
            if direct == 3:
                for i in range(down, up-1, -1):
                    res[i][left] = j
                    j += 1
                left += 1

            if left > right or up > down: return res
            direct = (direct + 1) % n

obj = Solution()
print(obj.generateMatrix(3))

"""
Let's say I have the following empty two dimensional array in Python:

q = [[None]*5]*4
I want to assign a value of 5 to the first row in the first column of q. Instinctively, I do the following:

q[0][0] = 5
However, this produces:

 [[5, None, None, None, None],
  [5, None, None, None, None],
  [5, None, None, None, None],
  [5, None, None, None, None]]
"""
