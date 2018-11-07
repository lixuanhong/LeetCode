"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.
Example 1:
Input:s1 = "ab" s2 = "eidbaooo"
Output:True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False
Note:
The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
"""

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        m, n = len(s1), len(s2)
        if m > n:
            return False
        vs1 = [0] * 26
        vs2 = [0] * 26
        for c in vs1:
            vs1[ord(c) - ord('a')] += 1
        for i in range(n):
            if i >= m:
                vs2[ord(s2[i - m]) - ord('a')] -= 1
            vs2[ord(s2[i]) - ord('a')] += 1
            if vs1 == vs2:
                return True
        return False
