"""
Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.
"""

"""
思路：其实这个题就考了一个相对顺序。s比较短，而t很长，那么尽量就对t进行一次遍历最好。可以使用一个队列保留s的每个元素，这样对t进行遍历，
如果遍历到的元素和队列的头元素相等，那么队列出头元素。这样最后返回队列是否为空即可。
"""
import collections
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        queue = collections.deque(s)
        for c in t:
            if not queue:
                return True        #s可能是“”
            if c == queue[0]:
                queue.popleft()
        return not queue          #如果queue被pop完了，那就就是True, 否则是False
