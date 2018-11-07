"""
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

"""

"""
思路：给出筛选数值范围，找出sqrt(n)以内的质数，质数的倍数肯定不是质数。
时间复杂度 O(NlglgN) 空间复杂度 O(N)
"""

class Solution(object):
    def countPrimes(self, n):
        if n < 3: return 0
        dp = [1] * n
        dp[0] = 0
        dp[1] = 0
        res = 0
        for i in range(2, int(n**0.5) + 1):         #找出i平方以内的质数就好，注意n**0.5是float, 要转换成为int
            if dp[i] == 1:
                for j in range(2*i, n, i):
                    dp[j] = 0
        return sum(dp)


# My Solution - 超时
class Solution(object):
    def countPrimes(self, n):
        count = 0
        for i in range(2, n):
            if self.isPrime(i):
                count += 1
        return count


    def isPrime(self, n):
        for i in range(2, n):
            if n % i != 0:
                continue
            else:
                return False
        return True
