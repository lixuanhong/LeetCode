"""
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
Note:
The input string length won't exceed 1000.
"""

class Solution(object):
    def countSubstrings(self, s):
        ans = 0
        for i in range(len(s)):
            ans += self.palindrom(s, i, i)
            ans += self.palindrom(s, i, i+1)
        return ans


    def palindrom(self, s, left, right):
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count















#===============================================================================
# 我的解法 - 超时！！
class Solution(object):
    def countSubstrings(self, s):
        res = 0
        if len(s) == 0: return res
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                list = [char for char in s[i:j]]
                if list[:] == list[::-1]:
                    res += 1
        return res

obj = Solution()
s = "abc"
print(obj.countSubstrings(s))
