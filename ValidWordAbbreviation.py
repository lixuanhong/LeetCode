"""
Given a non-empty string s and an abbreviation abbr, return whether the string matches with the given abbreviation.

A string such as "word" contains only the following valid abbreviations:

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
Notice that only the above abbreviations are valid abbreviations of the string "word". Any other string is not a valid abbreviation of "word".

Note:
Assume s contains only lowercase letters and abbr contains only lowercase letters and digits.

Example 1:
Given s = "internationalization", abbr = "i12iz4n":

Return true.
Example 2:
Given s = "apple", abbr = "a2e":

Return false.
"""
class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        idx, count = 0, 0
        for c in abbr:
            if c.isdigit():
                if c == '0' and count == 0:          #‘0’不能是一串数字的首字符！！
                    return False
                count = count * 10 + int(c)
            else:
                idx += count
                count = 0
                if idx >= len(word) or word[idx] != c:
                    return False
                idx += 1
        return idx + count == len(word)             #有可能abbr最后的字符是数字
