"""
Excel Sheet Column Title

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"

"""

"""
思路：可以理解为进制转化，将10进制数转化为每位以A-Z表示的26进制数。

使用Python解题时，需要使用ord()函数将字母转化为整数，使用chr()函数将整数转化回字母。
"""

class Solution(object):
    def convertToTitle(self, n):
        ans = ''
        while n:
            ans = chr(ord('A') + (n-1) % 26) + ans  #注意：ans放在加号后面，不能+=，容易出错！！
            n = (n - 1) / 26
        return ans
