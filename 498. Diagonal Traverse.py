"""
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

Example:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output:  [1,2,4,7,5,3,6,8,9]
Explanation:

Note:
The total number of elements of the given matrix will not exceed 10,000.
"""

"""
思路：由于移动的方向不再是水平或竖直方向，而是对角线方向，那么每移动一次，横纵坐标都要变化，向右上移动的话要坐标加上[-1, 1]，向左下移动的话要坐标加上[1, -1]，
那么难点在于我们如何处理越界情况，越界后遍历的方向怎么变换。向右上和左下两个对角线方向遍历的时候都会有越界的可能，但是除了左下角和右上角的位置越界需要改变两个坐标之外，
其余的越界只需要改变一个。那么我们就先判断要同时改变两个坐标的越界情况，即在右上角和左下角的位置。如果在右上角位置还要往右上走时，那么要移动到它下面的位置的，
那么如果col超过了n-1的范围，那么col重置为n-1，并且row自增2，然后改变遍历的方向。同理如果row超过了m-1的范围，那么row重置为m-1，并且col自增2，然后改变遍历的方向。
然后我们再来判断一般的越界情况，如果row小于0，那么row重置0，然后改变遍历的方向。同理如果col小于0，那么col重置0，然后改变遍历的方向。
"""

class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        m, n = len(matrix), len(matrix[0])
        r, c, k = 0, 0, 0
        res = []
        dir = [[-1, 1], [1, -1]]
        for i in range(m*n):
            res.append(matrix[r][c])
            r += dir[k][0]
            c += dir[k][1]
            if r >= m:
                r = m - 1
                c += 2
                k = 1 - k
            if c >= n:
                c = n - 1
                r += 2
                k = 1 - k
            if r < 0:
                r = 0
                k = 1 - k
            if c < 0:
                c = 0
                k = 1 - k
        return res
