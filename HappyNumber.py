"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example:

Input: 19
Output: true
Explanation:
1**2 + 9**2 = 82
8**2 + 2**2 = 68
6**2 + 8**2 = 100
1**2 + 0**2 + 0**2 = 1
"""
# Correct Solution
class Solution(object):
    def isHappy(self, n):
        numset = set()
        while n != 1 and n not in numset:
            numset.add(n)
            sum = 0
            while n:
                digit = n % 10
                sum += digit * digit
                n = n // 10
            n = sum
        return n == 1




# My Solution - 无法终止程序
class Solution(object):
    def isHappy(self, n):
        if n == 0: return False
        if n == 1: return True
        tmp = n
        while True:
            while tmp < 10:
                tmp = tmp ** 2
            tmp = str(tmp)
            sum = 0
            for i in range(len(tmp)):
                sum += int(tmp[i])**2
            if sum == 1: return True
            tmp = sum

obj = Solution()
print(obj.isHappy(82))
