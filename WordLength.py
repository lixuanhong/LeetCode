"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        list = s.split(" ")
        n = len(list)
        if n == 0:
            return 0
        for i in range(n):
            if list[n-1-i] != "":
                return len(list[n-1-i])
        return 0

obj = Solution()
s = "Hello World"
print(obj.lengthOfLastWord(s))

"""
s="a "
print(s.split(" ")) #['a', '']
"""
