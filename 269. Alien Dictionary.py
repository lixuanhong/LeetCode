"""
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
Example 2:

Input:
[
  "z",
  "x"
]

Output: "zx"
Example 3:

Input:
[
  "z",
  "x",
  "z"
]

Output: ""

Explanation: The order is invalid, so return "".
Note:

You may assume all letters are in lowercase.
You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
"""

"""
https://segmentfault.com/a/1190000003795463
思路：拓扑排序。我们首先要初始化所有节点（即字母），一个是该字母指向的字母的集合（被指向的字母在字母表中处于较后的位置），一个是该字母的计数器。
然后我们根据字典开始建图，但是字典中并没有显示给出边的情况，如何根据字典建图呢？其实边都暗藏在相邻两个词之间，比如abc和abd，我们比较两个词的每一位，
直到第一个不一样的字母c和d，因为abd这个词在后面，所以d在字母表中应该是在c的后面。所以每两个相邻的词都能蕴含一条边的信息。在建图的同时，实际上我们也可以计数了，
对于每条边，将较后的字母的计数器加1。计数时需要注意的是，我们不能将同样一条边计数两次，所以要用一个集合来排除已经计数过的边。最后，我们开始拓扑排序，
从计数器为0的字母开始广度优先搜索。为了找到这些计数器为0的字母，我们还需要先遍历一遍所有的计数器。

最后，根据结果的字母个数和图中所有字母的个数，判断时候有环即可。无环直接返回结果。
Time Complexity: O(N) Space Complexity: O(N)

图 -> 入度为0 -> BFS
"""

from sets import Set

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if not words or len(words) = 0:
            return ""

        if len(words) == 1:
            return "".join([s for s in Set(words[0])])

        #len(words) >= 2


    def build_graph(self, words):
        dict = {}
        int degree = [0] * 26
        int count = 0

        for word in words:
            for c in word:
                if degree[ord(c) - ord('a')] == 0:
                    count += 1
                    degree[ord(c) - ord('a')] = 1

        for i in range(len(words) - 1):
            cur = words[i]
            next = words[i+1]
            len = min(cur, next)
            for j in range(len):
                if cur[j] != next[j]:
                    if cur[j] not in dict:
                        dict
