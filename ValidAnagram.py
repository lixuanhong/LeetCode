"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

"""

class Solution:
    def isAnagram(self, s, t):
        s_sorted = ''.join(sorted(s))   #sorted将字符串变成数组, 也可以不用join
        t_sorted = ''.join(sorted(t))
        return s_sorted == t_sorted

obj = Solution()
s = "rat"
t = "car"
print(obj.isAnagram(s, t))
