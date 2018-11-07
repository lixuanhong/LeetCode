"""
Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
"""

"""
思路：要找s[i,j]的最大子串，先统计频数，然后遍历一遍频数，找出第一个频数小于k且大于0的字符，然后找出这个字符的位置，
接下来的分析很重要，这个字符一定不能出现在任何的子串中，因为i,j是整个的子串，在ij里面频数都没有达到k，那么在ij的任何子串中，
这个字符也不可能达到频数k。所以不能有这个字符，那么就在这个位置做一个分治，返回前半部分和后半部分的最大值。

https://blog.csdn.net/u010900754/article/details/62159601?utm_source=copy
"""

import collections
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) < k:
            return 0
        counter = collections.Counter(s)
        for c, v in counter.items():
            if v < k:
                return max([self.longestSubstring(sub, k) for sub in s.split(c)])
        return len(s)
