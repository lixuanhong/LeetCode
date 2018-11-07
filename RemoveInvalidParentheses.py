"""
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]

"""

"""
方法：DFS。首先检查s是否合法：两个条件：任何时候右括号数量<=左括号数量，最终右括号数量=左括号数量。
l和r表示需要删除的左括号和右括号数量，先删除右括号再删除左括号。当有两个连续括号时，删除前面第一个括号
就可以了，不会有重复解。

dfs(s, l, r):
    if l == 0 and r == 0 and valid(s):
        ans.add(s)
Time Complexity: O(2^n)
Space Complexity: O(2^n)
"""
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        l, r = 0, 0
        for c in s:
            if c == "(":
                l += 1
            if c == ")":
                if l == 0:
                    r += 1
                else:
                    l -= 1

        res = []
        self.dfs(s, 0, l, r, res)
        return res

    def isValid(self, s):
        count = 0
        for c in s:
            if c == "(":
                count += 1
            if c == ")":
                count -= 1
            if count < 0:
                return False
        return count == 0

    def dfs(self, s, start, l, r, res):
        if l == 0 and r == 0:
            if self.isValid(s):
                res.append(s)
                return

        for i in range(start, len(s)):
            if i != start and s[i] == s[i-1]:              #only remove the first parentheses if there are consecutive ones to avoid duplication
                continue

            if l > 0 and s[i] == "(":
                cur = s[:i] + s[i+1:]
                self.dfs(cur, i, l-1, r, res)
            if r > 0 and s[i] == ")":
                cur = s[:i] + s[i+1:]
                self.dfs(cur, i, l, r-1, res)
