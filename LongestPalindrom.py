"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

class Solution(object):
    def longestPalindrome(self, s):
        def palindrome(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1: right]

        ans = ''
        for i in range(len(s)):
            pal1 = palindrome(s, i, i)
            if len(pal1) > len(ans): ans = pal1
            pal2 = palindrome(s, i, i+1)
            if len(pal2) > len(ans): ans = pal2
        return ans

"""
回文有两种形式：(1)aabb,(2)aacbb
遍历字符串每个位置分别考虑这两种情况，找到最长的回文子字符串
"""
