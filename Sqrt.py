"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.
"""
# import math
# class Solution(object):
#     def mySqrt(self, x):
#         return int(math.sqrt(x))

"""
math.sqrt(8) # 2.8284271247461903
int(math.sqrt(8))
"""

#这道题考察binary search, 只返回整数部分
class Solution(object):
    def mySqrt(self, x):
        if x == 0 or x == 1:
            return x
        i = 1; j = x/2
        last = 0
        while i <= j:
            mid = (i+j)/2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 > x:
                j = mid - 1
            else:
                i = mid + 1
                last = mid
        return int(last)

obj = Solution()
print(obj.mySqrt(64))
