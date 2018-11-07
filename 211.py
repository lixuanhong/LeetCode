"""
Add and Search Word - Data Structure Design

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
思路：这道题如果做过之前的那道 Implement Trie (Prefix Tree) 实现字典树(前缀树)的话就没有太大的难度了，还是要用到字典树的结构，
唯一不同的地方就是search的函数需要重新写一下，因为这道题里面'.'可以代替任意字符，所以一旦有了'.'，就需要查找所有的子树，只要有一个返回true，
整个search函数就返回true，典型的DFS的问题，其他部分跟上一道实现字典树没有太大区别。
"""

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """



    def addWord(self,word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """


    def search(self.word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
