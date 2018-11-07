"""
A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:

For 1-byte character, the first bit is a 0, followed by its unicode code.
For n-bytes character, the first n-bits are all one's, the n+1 bit is 0, followed by n-1 bytes with most significant 2 bits being 10.
This is how the UTF-8 encoding would work:

   Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
Given an array of integers representing the data, return whether it is a valid utf-8 encoding.

Note:
The input is an array of integers. Only the least significant 8 bits of each integer is used to store the data. This means each integer represents only 1 byte of data.

Example 1:

data = [197, 130, 1], which represents the octet sequence: 11000101 10000010 00000001.

Return true.
It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.
Example 2:

data = [235, 140, 4], which represented the octet sequence: 11101011 10001100 00000100.

Return false.
The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
The next byte is a continuation byte which starts with 10 and that's correct.
But the second continuation byte does not start with 10, so it is invalid.
一个UTF8字符的长度从1到4个字节不等，服从下列规则：
对于1字节的字符，首位数是0，后面是unicode代码。
对于n字节的字符，前n位数全是1，第n+1位是0，后面跟着n-1个字节，最高位的两位数是10。
详见上表。
给定一个整数数组表示的数据，判断其是否为有效的utf-8编码。
注意：
输入是整数数组。只有最低位的8位数用来存放数据。这意味着每一个整数只表示一个字节的数据。
"""

class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        count = 0
        for d in data:
            if count == 0:
                if d >> 5 == 0b110:
                    count = 1
                elif d >> 4 == 0b1110:
                    count = 2
                elif d >> 3 == 0b11110:
                    count = 3
                elif d >> 7:
                    return False
            else:
                if d >> 6 != 0b10:
                    return False
                count -= 1
        return count == 0
