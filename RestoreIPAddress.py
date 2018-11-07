"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
"""

#思路：IP地址由四部分构成，可以设置一个变量segment,当segment = 4时，可结束循环，将结果添加到列表中；
#每个部分数值均值0---255之间，因此每次回溯最多需要判断3个元素，即当前元素i---i+2这三位数字。

class Solution(object):
    def restoreIpAddresses(self, s):
        def dfs(s, seg, ip, res):
            if seg == 4:
                if s == '':
                    res.append(ip[1:]) #把最开始的‘.’去掉
                return
            for i in range(1, 4): # i = 1, 2, 3
                if i <= len(s):        # if i > len(s), s[:i] will make false!!
                    if int(s[:i]) <= 255:    # i not inclusive最多取三位
                        dfs(s[i:], seg+1, ip+"."+s[:i], res)
                        if s[0] == '0':  # make sure that res just can be '0.0.0.0' and remove like '00'
                            break
        res = []
        dfs(s, 0, '', res)
        return res
