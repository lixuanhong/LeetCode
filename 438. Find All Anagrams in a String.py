"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""


#sliding window 两个Array来记录比较
class Solution(object):
    def findAnagrams(self, s, p):
        m, n = len(s), len(p)
        res = []
        vs = [0] * 26
        vp = [0] * 26
        for c in p:
            vp[ord(c) - ord('a')] += 1
        for i in range(m):
            if i >= n:
                vs[ord(s[i-n]) - ord('a')] -= 1
            vs[ord(s[i]) - ord('a')] += 1
            if vs == vp:
                res.append(i-n+1)
        return res




# Time Limit Exceed
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n = len(p)
        res = []
        if len(s) == 0 or s is None: return res
        for i in range(len(s) - n + 1):
            if self.isAnagrams(s[i:i+n], p):
                res.append(i)
        return res



    def isAnagrams(self, num1, num2):
        if len(num1) != len(num2):
            return False
        array = [0] * 26
        for c in num1:
            array[ord(c) - ord('a')] += 1
        for c in num2:
            if array[ord(c) - ord('a')] == 0:
                return False
            array[ord(c) - ord('a')] -= 1
        for item in array:
            if item != 0:
                return False
        return True
