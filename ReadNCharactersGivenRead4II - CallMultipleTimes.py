"""
Read N Characters Given Read4 II - Call multiple times

The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Note:
The read function may be called multiple times.

Example 1:

Given buf = "abc"
read("abc", 1) // returns "a"
read("abc", 2); // returns "bc"
read("abc", 1); // returns ""
Example 2:

Given buf = "abc"
read("abc", 4) // returns "abc"
read("abc", 1); // returns ""

"""

"""
这道题是157的升级版，这里要求目标函数能够被多次调用。所以出现了一个情况，就是上次read4()读回来的字符还没完全被取完。我们要先去buffer里面取，
取不到了后才再次调用read4()函数去读字符。
https://blog.csdn.net/foolnote/article/details/50626162
"""

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):

    def __init__(self):
        self.index = 0
        self.count = 0
        self.buf4 = [""] * 4                          #用全局变量

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        actRead = 0
        isEnd = False
        while !isEnd and actRead < n:
            if self.count == 0:                       #这个条件很重要，因为self.count是全局变量
                self.count = read4(self.buf4)
                if self.count < 4:
                    isEnd = True

            while self.count > 0 and actRead < n:     #如果上次读取的数字在self.count中还有残余，那么就直接在残余的部分里面读取，保证了顺序！！
                buf[actRead] = self.buf4[self.index]
                actRead += 1
                self.index += 1
                self.count -= 1
                self.index = self.index % 4
       return actRead
