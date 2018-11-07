"""
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:
Input: 3
Output: False
"""

import math
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        a, b = 0, int(math.sqrt(c))                #sqrt计算出来包括小数，要取整
        while a <=b:                               #注意：这道题目里面a和b可以相等！！
            if a*a + b*b == c:
                return True
            elif a*a + b*b < c:
                a += 1
            else:
                b -= 1
        return False
