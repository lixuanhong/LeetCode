"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Returns: True
Example 2:

Input: 14
Returns: False
"""

class Solution(object):
    def isPerfectSquare(self, num):
        if num == 1:
            return True
        i = 0
        j = num
        while i < j:
            mid = (i+j)/2
            if mid ** 2 == num:
                return True
            elif mid ** 2 < num:
                i = mid + 1
            else:
                j = mid
        return False

obj = Solution()
print(obj.isPerfectSquare(4))
