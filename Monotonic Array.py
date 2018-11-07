"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.



Example 1:

Input: [1,2,2,3]
Output: true
Example 2:

Input: [6,5,4,4]
Output: true
Example 3:

Input: [1,3,2]
Output: false
Example 4:

Input: [1,2,4,5]
Output: true
Example 5:

Input: [1,1,1]
Output: true


Note:

1 <= A.length <= 50000
-100000 <= A[i] <= 100000
"""

"""
思路：遍历数组，标记升序/降序情况。当发现后面的元素与前面的标记冲突时，则返回 false, 否则返回 true。
"""

class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        flag = 0  #1表示降序 2表示升序
        for i in range(len(A) - 1):
            if A[i+1] > A[i]:
                if flag == 0: flag = 2
                elif flag == 1: return False
            elif A[i+1] < A[i]:
                if flag == 0: flag = 1
                elif flag == 2: return False
        return True 
