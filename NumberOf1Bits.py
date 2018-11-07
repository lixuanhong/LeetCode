"""
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Example 1:

Input: 11
Output: 3
Explanation: Integer 11 has binary representation 00000000000000000000000000001011
Example 2:

Input: 128
Output: 1
Explanation: Integer 128 has binary representation 00000000000000000000000010000000
"""
"""
Time O(1) Space O(1)
通过与运算符判断最低位/最高位是否是1，然后再右移/左移。重复此步骤直到原数归零。

"""

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n != 0b0:
            res += (n & 1)
            n = n >> 1
        return res 
