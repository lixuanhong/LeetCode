"""
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
"""

"""
思路：利用stack数据结构，当出现左括号时，将字符串压栈；当出现右括号时，将字符串弹栈，并重复响应次数，累加至新的栈顶元素。
"""

import collections
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        k = 1
        contents = collections.defaultdict(str)
        times = collections.defaultdict(int)
        for c in s:
            if c.isdigit():
                times[k] += times[k] * 10 + int(c)
            elif c == "[":
                k += 1
            elif c == "]":
                contents[k-1] += times[k-1] * contents[k]
                times[k-1] = 0
                contents[k] = ""
                k -= 1
            else:
                contents[k] += c
        return contents[1]
