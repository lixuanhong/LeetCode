"""
Excel Sheet Column Number

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
"""

class Solution(object):
    def titleToNumber(self, s):
        n = len(s)
        ans = 0
        for character in s:
            ans += (ord(character) - ord('A') + 1) * 26 ** (n-1)
            n = n - 1
        return ans

obj = Solution()
s = "ZY"
print(obj.titleToNumber(s))
