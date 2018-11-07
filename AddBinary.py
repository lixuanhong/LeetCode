"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

"""
#思路：从两个字符串的最低位开始，一位一位的进行二进制相加，并保存进位，最终可以得到两者的和的字符串。
class Solution(object):
    def addBinary(self, a, b):
        i = len(a) - 1
        j = len(b) - 1
        res = ''
        plus = 0
        while i >= 0 or j >= 0 or plus == 1:
            plus += int(a[i]) if i >= 0 else 0
            plus += int(b[j]) if j >= 0 else 0
            res = str(plus % 2) + res
            i, j, plus = i - 1, j - 1, plus/2
        return res
#如果是八进制，把2改成8就可以了

#递归实现：当两个加数都是1时要进位
class Solution(object):
    def addBinary(self, a, b):
        if not a or not b:
            return a if a else b
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[:-1], b[:-1]), '1') + '0'
        elif a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[:-1], b[:-1]) + '0'
        else:
            return self.addBinary(a[:-1], b[:-1]) + '1'
