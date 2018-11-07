"""
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].
"""

import collections
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        counter = collections.Counter(S)
        res = "#"                          #初始res必须有个字符，否则res[-1]会出现错误！
        while counter:
            stop = True
            for c, times in counter.most_common():   #counter.most_common()返回的是一个pair
                if res[-1] != c:
                    res += c
                    counter[c] -= 1
                    if counter[c] == 0:
                        del counter[c]              #del counter[key] remove the key completely
                    stop = False
                    break
            if stop: break
        return res[1:] if len(res) == len(S)+1 else ""
