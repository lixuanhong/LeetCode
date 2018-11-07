"""
Write a function that takes a string as input and returns the string reversed.

Example 1:

Input: "hello"
Output: "olleh"
Example 2:

Input: "A man, a plan, a canal: Panama"
Output: "amanaP :lanac a ,nalp a ,nam A"

"""

class Solution(object):
    def reverseString(self, s):
        if len(s) == 0:
            return ""

        s = list(s)             #string is not mutable; convert to list, will keep whitespace
        for i in range(0, len(s)/2):
            tmp = s[i]
            s[i] = s[len(s) - 1 - i]
            s[len(s) - 1 - i] = tmp
        return ''.join(s)
