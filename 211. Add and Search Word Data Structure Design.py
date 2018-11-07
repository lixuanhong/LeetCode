"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
"""

"""
思路：使用Trie实现，查找的时候用递归处理'.'的情况。
"""

class TrieNode:
    def __init__(self):
        self.leaf = False
        self.children = [None] * 26

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.size = 0

    def insert(self, s):
        if len(s) == 0:
            return
        p = self.root
        for i in range(len(s)):
            if p.children[ord(s[i]) - ord('a')] is None:
                new_node = TrieNode()
                p.children[ord(s[i]) - ord('a')] = new_node
            p = p.children[ord(s[i]) - ord('a')]
        p.leaf = True
        self.size += 1

    def search(self, s):
        if len(s) == 0:
            return False

        return self.searchRe(s, self.root, 0)

    def searchRe(self, s, p, i):
        if len(s) == i:                   #这是递归的终止条件！！！
            if p.leaf:
                return True
            return False

        result = False
        if s[i] == '.':
            for j in range(0, 26):
                if p.children[j] != None:
                    if self.searchRe(s, p.children[j], i+1):   #注意：这里必须是递归判断！！要所有递归路径都是true, 结果才是true
                        result = True
        else:
            if p.children[ord(s[i]) - ord('a')] != None:
                if self.searchRe(s, p.children[ord(s[i]) - ord('a')], i + 1):
                    result = True
        return result


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()


    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.trie.insert(word)


    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.trie.search(word)
