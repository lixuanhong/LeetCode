"""
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]
"""

#递归求解
class Solution:
    def myPow(self, x, n):
        if n == 0:
            return 1
        elif n < 0:
            return 1 / self.myPow(x, -n)
        elif n % 2:
            return self.myPow(x*x, n//2) * x #注意：python3里面除法取整必须用//
        else:
            return self.myPow(x*x, n//2)



# My Solution - Time Limit Input (0.00001, 21458964)
class Solution:
    def myPow(self, x, n):
        if n == 0: return 1
        if x == 0: return 0
        product = 1
        for i in range(abs(n)):
            if n > 0:
                product = product * x
            if n < 0:
                product = product * 1/abs(x)
        return product

obj = Solution()
print(obj.myPow(2.0, -2))
