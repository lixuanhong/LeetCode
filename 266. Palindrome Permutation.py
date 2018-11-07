"""
Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false
Example 2:

Input: "aab"
Output: true
Example 3:

Input: "carerac"
Output: true
"""

class Solution(object):
    def canPermutePalindrome(self, s):
        res = []
        for c in s:
            if c not in res:
                res.append(c)
            else:
                res.remove(c)
        if len(res) == 0 or len(res) == 1:
            return True
        else:
            return False 
