"""
The count-and-say sequence is the sequence of integers with the first five terms as following:
1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
"""

#题目大意:

#n=1 返回1
#n=2由于n=1的结果为1，有1个1，所以返回11
#n=3由于n=2结果为11，有2个1，返回21
#n=4由于n=3结果为21，有1个2和1个1，所以返回1211
#给定n,以此类推

class Solution(object):
    def countAndSay(self, n):
         def count(s):
            res = ""
            count = 1
            for idx, value in enumerate(s):
                if idx < len(s) - 1 and s[idx] != s[idx+1]:   #因为要从第一个元素开始，所以比较idx和idx+1；要判断idx < len(s) - 1
                    res += str(count) + value
                    count = 1
                elif idx < len(s) - 1:
                    count += 1
            res += str(count) + value             #对最后一个元素操作
            return res

        s = "1"
        for i in range(1, n):
            s = count(s)             #初始化s = "1", 所以循环n-1次就可以得到结果
        return s

obj = Solution()
print(obj.countAndSay(6)) #312211
