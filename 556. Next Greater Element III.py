"""
Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.

Example 1:

Input: 12
Output: 21


Example 2:

Input: 21
Output: -1
"""

"""
思路：和31.Next Permutation解题方法基本一模一样，先找到从后向前数，第一个降序的位置，
把此位置后面的翻转。再把这个降序数字和后面第一个比它大的位置交换即可。
"""
class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = list(str(n))
        if len(num) <= 1: return -1
        partition = -1
        for i in range(len(num) - 2, -1, -1):
            if int(num[i]) < int(num[i+1]):
                partition = i
                break
        if partition == -1:
            return -1
        for j in range(len(num) - 1, partition, -1):
            if int(num[j]) > int(num[partition]):
                num[partition], num[j] = num[j], num[partition]
                break
        num[partition + 1:len(num)] = num[partition+1:len(num)][::-1]
        res = int("".join(num))
        if res > 1 << 31:                       #注意：这里有32位整数的要求！！python 3已经没有maxint的limit了，所以这里用位操作
            return -1
        else:
            return res
