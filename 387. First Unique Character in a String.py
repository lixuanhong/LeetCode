"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
"""

class Solution(object):
    def firstUniqueChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or s == None: return -1
        array = [0] * 26
        res = 0x7FFFFFFF
        for c in s:
            array[ord(c) - ord('a')] += 1
        for i in range(len(array)):
            if array[i] == 1:
                if s.index(chr(i + ord('a'))) < res:
                    res = s.index(chr(i + ord('a')))
        return res if res != 0x7FFFFFFF else -1
