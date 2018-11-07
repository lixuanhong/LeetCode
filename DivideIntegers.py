"""
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
"""
class Solution(object):
    def divide(self, dividend, divisor):
        if abs(dividend) < abs(divisor):
            return 0
        a = abs(dividend)
        b = abs(divisor)
        count = 0
        sum = 0
        res = 0
        while a >= b:
            sum = b
            count = 1
            while sum + sum <= a:
                sum += sum
                count += count
            a -= sum
            res += count
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            res = 0 - res
            return max(-2**31, res)
        return min(2**31-1, res)



# My Solution - Time Limite Exceed O(n)
class Solution(object):
    def divide(self, dividend, divisor):
        if dividend == 0: return 0
        i = 0
        tmp = dividend
        while abs(tmp) >= abs(divisor):
            tmp = abs(tmp) - abs(divisor)
            i += 1
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            return min(i, 2**31 - 1)
        elif (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            return max(-i, -2**31-1)

obj = Solution()
print(obj.divide(-1, 1))
