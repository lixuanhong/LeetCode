"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false
"""

"""
思路：可以用DFS但是写法复杂；NB写法，Time Complexity O(N) Space Complexity O(N)

例子： “bbarc”
      "b*c"
"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        idxs, idxp = 0, 0
        match = 0
        star = -1
        while idxs < len(s):
            if idxp < len(p) and (p[idxp] == s[idxs] or p[idxp] == "?"):
                idxp += 1
                idxs += 1
            elif idxp < len(p) and p[idxp] == "*":
                star = idxp
                match = idxs
                idxp += 1
            elif star != -1:
                idxp = star + 1
                match += 1
                idxs = match
            else:
                return False
        while idxp < len(p) and p[idxp] == "*":
            idxp += 1
        return idxp == len(p)
