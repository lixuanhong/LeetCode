"""
Read N Characters Given Read4

The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Example 1:

Input: buf = "abc", n = 4
Output: "abc"
Explanation: The actual number of characters read is 3, which is "abc".
Example 2:

Input: buf = "abcde", n = 5
Output: "abcde"

time: O(n)
space: O(1)
"""

"""
思路：O(N) O(1)

通过使用API int read4(char *buf)每次从文件读取四个字符，返回读取字符的数量，来实现int read(char *buf, int n)即从文件中读取n个字符，然后返回实际读取的字符数量。
注意*buf实际上是一个tmp数组，来存放每次从文件读取的字符, 并不是我们需要读取的数组。本题是从文件读取！！另外，要求返回的值是实际读取字符的数量count, 可能<=n,
并不是实际的数组，这一点需要确认。
"""

#Note: the read function will only be called once for each test case.

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        count = 0
        buf4 = [""]*4               #实际上是建立一个container来存放read4读取的字符，这个是API的要求
        while count < n:
            num = read4(buf4)       #用read4方法，把读取存放到buf4里面
            if num == 0: break
            index = 0
            while index < num and count < n:
                buf[count] = buf4[index]        #同样的，buf也是一个container来存放读取的字符
                count += 1
                index += 1
        return count
