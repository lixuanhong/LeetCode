"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""


"""
解题思路：解码有多少种方法。一般求“多少”我们考虑使用dp。状态方程如下：

　　　　　当s[i-2:i]这两个字符是10~26但不包括10和20这两个数时，比如21，那么可以有两种编码方式（BA，U），所以dp[i]=dp[i-1]+dp[i-2]

　　　　　当s[i-2:i]等于10或者20时，由于10和20只有一种编码方式，所以dp[i]=dp[i-2]

　　　　   当s[i-2:i]不在以上两个范围时，如09这种，编码方式为0，而31这种，dp[i]=dp[i-1]。

　　　　   注意初始化时：dp[0]=1,dp[1]=1
"""



class Solution(object):
    def numDecodings(self, s):
        if s == "" or s[0] == '0': return 0   #第一位出现0的编码是不合法的
        if len(s) == 1: return 1
        dp = [0] * (len(s) + 1)
        dp[0], dp[1] = 1, 1      #在动态规划过程中，最终所有的字符会削减为0，dp[0] = 1
        for i in range(2, len(s)+1):   # 这里dp[len(s)]记录的是s[len(s) -1]前的所有组合，因为dp[0]占用了一位
            if 10 < int(s[i-2: i]) <= 26 and int(s[i-2: i]) != 20:
                dp[i] = dp[i-1] + dp[i-2]
            elif int(s[i-2:i]) == 10 or int(s[i-2:i]) == 20:
                dp[i] == dp[i-2]
            elif s[i-1] != '0':    #这个条件很重要，排除了“09”；超过26的数字只能考虑前面一位
                dp[i] = dp[i-1]
            else:                  #"0"在数字前的编码方式为0，比如“26609”无法编码！！
                return 0
        return dp[len(s)]





obj = Solution()
print(obj.numDecodings("226"))
