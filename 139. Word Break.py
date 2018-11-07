"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""

"""
动态规划
https://www.youtube.com/watch?v=ptlwluzeC1I
"""


#用memo,好理解
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        return self.canBreak(s, {}, wordDict)


    def canBreak(self, s, m, wordDict):
        if s in m: return m[s]            #注意：这里return m[s]
        if s in wordDict:
            m[s] = True
            return True

        for i in range(1, lens(s)):
            r = s[i:]
            if r in wordDict and self.canBreak(s[0:i], m, wordDict):
                m[s] = True
                return True
        m[s] = False
        return False


#更简洁的dp
class Solution(object):
    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):                      #注意：两个for循环
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        return dp[len(s)]
