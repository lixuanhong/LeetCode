"""
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
"""

class TrieNode(object):
    def__init__(self):
        self.leaf = False
        self.children = [None] * 26

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        self.size = 0


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        if len(word) == 0:
            return
        p = self.root
        for i in range(len(word)):
            if p.children[ord(word[i]) - ord('a')] is None:
                new_node = TrieNode()
                p.children[ord(word[i]) - ord('a')] = new_node
            p = p.children[ord(word[i]) - ord('a')]
        p.leaf = True
        self.size += 1

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if len(word) == 0:
            return False
        return self.searchRe(word, self.root, 0)

    def searchRe(self, word, p, i):
        if len(word) == i:
            if p.leaf:
                return True
            return False

        if p.children[ord(word[i]) - ord('a')] != None:
            if self.searchRe(word, p.children[ord(word[i]) - ord('a')], i+1):
                return True
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        p = self.root()
        for c in prefix:
            if p.children(ord(c) - ord('a')) is None:
                return False
            p = p.children(ord(c) - ord('a'))
        return True
