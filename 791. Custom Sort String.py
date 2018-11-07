"""
S and T are strings composed of lowercase letters. In S, no letter occurs more than once.

S was sorted in some custom order previously. We want to permute the characters of T so that they match the order that S was sorted. More specifically, if x occurs before y in S, then x should occur before y in the returned string.

Return any permutation of T (as a string) that satisfies this property.

Example :
Input:
S = "cba"
T = "abcd"
Output: "cbad"
Explanation:
"a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a".
Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid outputs.


Note:

S has length at most 26, and no character is repeated in S.
T has length at most 200.
S and T consist of lowercase letters only.
"""

"""
使用字典保存T中的每个字母出现的次数，然后遍历S中的每个字符，查表构建新的结果字符串，并且把已经遍历了的字符的次数设为0。最后把count中剩余的字符放到最后。

这里用到了一个技巧，Counter中使用不存在的索引会返回0.

如：

from collections import Counter
count = Counter("Hello World!")
print count['8']
##输出0

https://blog.csdn.net/fuxuemingzhu/article/details/79378688?utm_source=copy
"""

import collections
class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        counter = collections.Counter(T)
        res = ""
        for s in S:
            res += s * counter[s]
            counter[s] = 0                  #把已经排序过的字母设为0
        for c in counter:                   #对字典里面T包含的除S外剩下字母进行排列！！注意这里遍历的是counter, 而不是T！！！
            res += c * counter[c]
        return res
