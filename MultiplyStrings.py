"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

"""
思路：两个非负数字字符串的相乘。其实就是大数乘法。算法的关键是要先将两个字符串翻转过来，然后按位进行相乘，相乘后的数不要着急进位，而是存储在一个数组里面，
然后将数组中的数对10进行求余（%），就是这一位的数，然后除以10，即/10，就是进位的数。注意最后要将相乘后的字符串前面的0去掉。

"""

class Solution:
    def multiply(self, num1, num2):
        num1 = num1[::-1]                       #将字符串顺序颠倒
        num2 = num2[::-1]
        res = [0] * (len(num1) + len(num2))

        for i in range(len(num1)):
            for j in range(len(num2)):
                res[i+j] += int(num1[i])*int(num2[j])

        carry = 0
        for i in range(len(res)):
            res[i], carry = (res[i] + carry) % 10, (res[i] + carry) // 10

        res = map(str, res)                   #将数字list转换成字符list
        product = "".join(res)[::-1]          #join字符list的顺序颠倒
        start = 0
        while start < len(product) and product[start] == '0':
            start += 1
        return product[start:] if start < len(product) else '0'


"""
string.join(iterable)

s = "-";
seq = ("a", "b", "c"); # This is sequence of strings.
print s.join( seq ) #a-b-c
"""
