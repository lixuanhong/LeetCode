"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

Example 1:

Input:  "69"
Output: true
Example 2:

Input:  "88"
Output: true
Example 3:

Input:  "962"
Output: false
"""

Time-O(n) Space-O(1)
class Solution(object):
    def isStrobogrammatic(self, num):
        left, right = 0, len(num)-1
        dict = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
        while left <= right:
            if num[left] not in dict:
                return False
            elif dict.get(num[left]) != num[right]:
                return False
            else:
                left -= 1
                right += 1
        return True




Time-O(n) Space-O(n)
class Solution(object):
    def isStrobogrammatic(self, num):
        s = ""
        dict = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
        for n in num:
            if n not in dict:
                return False
            s += dict.get(n)
        return num == s[::-1]               #注意：return的是s[::-1]
