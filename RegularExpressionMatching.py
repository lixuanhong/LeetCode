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

"aa", ".*" true
"ab", ".*" true
"aab", "c*aab" true
"aab", "c*a*b" true c* -> empty

"""

"""
思路：动态规划
dp[i][j]的含义是s[0-i]与p[0-j]是否匹配；dp[0][0] = true

1. p[j] == s[i]: dp[i][j] = dp[i-1][j-1]  "aa", "aa"
2. p[j] == ".": dp[i][j] = dp[i-1][j-1]   "aa", "a."
3. p[j] == "*":
   here are two sub conditions:
   1. if p[j-1] != s[i]: dp[i][j] = dp[i][j-2] //in this case, a* counts as empty  "baab", "bc*aab"
   2. if p[j-1] == s[i] or p[j-1] == '.':                              "aa", "a*"    "aa", ".*"
      dp[i][j] = dp[i][j-1] // in this case, a* counts as single a     "aa", "a*"
      dp[i][j] = dp[i-1][j] // in this case, a* counts as multiple a    "aaa", "a*"
      dp[i][j] = dp[i][j-2] // in this case, a* counts as empty
"""
class Solution:
    def isMatch(self, s, p):
        dp=[[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        dp[0][0]=True

        #预处理 ”aab“ ”c*aab“情况
        for i in range(1,len(p)+1):
            if p[i-1]=='*':
                if i>=2:
                    dp[0][i]=dp[0][i-2]

        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1]=='.':
                    dp[i][j]=dp[i-1][j-1]
                elif p[j-1]=='*':
                    dp[i][j]=dp[i][j-1] or dp[i][j-2] or (dp[i-1][j] and (s[i-1]==p[j-2] or p[j-2]=='.'))
                else:
                    dp[i][j]=dp[i-1][j-1] and s[i-1]==p[j-1]
        return dp[len(s)][len(p)]
