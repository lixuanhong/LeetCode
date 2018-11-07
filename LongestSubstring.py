"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
#思路：从左往右扫描，当遇到重复字母时，以上一个重复字母的index +1，作为新的搜索起始位置。直到扫描到最后一个字母。
class Solution:
    def lengthOfLongestSubstring(self, s):
        start = len_max = 0
        char_dict = {}
        for i in range(len(s)):
            if s[i] in char_dict and start <= char_dict[s[i]]:
                start = char_dict[s[i]] + 1
            else:
                len_max = max(len_max, i - start + 1)
            char_dict[s[i]] = i
        return len_max

obj = Solution()
print(obj.lengthOfLongestSubstring("pwwkew"))
