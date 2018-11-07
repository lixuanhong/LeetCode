"""
Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]
Example 2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]
Note:
The value k is positive and will always be smaller than the length of the sorted array.
Length of the given array is positive and will not exceed 104
Absolute value of elements in the array and x will not exceed 104

"""

#最佳解法 Time O(lgN) Space O(1)
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        left, right = 0, len(arr) - k           #这里right是len(arr) - k
        while left < right:
            mid = (left + right) / 2
            if x - arr[mid] > arr[mid+k] - x:    #这里用abs和不用abs对结果没有影响！
                left = mid + 1
            else:
                right = mid
        return arr[left: left+k]             #最后返回arr[left: left+k]
