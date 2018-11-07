"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""

"""
思路：sliding window, 尾指针不断往后扫，当扫到有一个窗口包含了所有T的字符，然后再收缩头指针，直到不能再收缩为止。最后记录所有可能的情况中窗口最小的。
time: O(N)
space: O(1)
"""

import collections
class Solution(object):
    def minWindow(self, s, t):
        counter = collections.Counter(t)
        idx = 0
        l = r = 0
        total = len(t)
        min = float("inf")
        for r in range(len(s)):
            if s[r] in counter:
                if counter[s[r]] > 0:
                    total -= 1
                counter[s[r]] -= 1

            while total == 0:
                if r - l + 1 < min:
                    min = r - l + 1
                    idx = l
                if s[l] in counter:
                    counter[s[l]] += 1
                    if counter[s[l]] > 0:
                        total += 1
                l += 1
        return "" if min == float("inf") else s[idx: idx+min]
