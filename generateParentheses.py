"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
class Solution(object):
    def generateParenthesis(self, n):
        return self.generate("", 0, 0, n, [])

    def generate(self, str, left, right, n, list):
        if left < n:
            self.generate(str+"(", left+1, right, n, list)
        if right < left:
            self.generate(str+")", left, right+1, n, list)
        if left == n and right == n:
            list.append(str)
        return list

obj = Solution()
print(obj.generateParenthesis(3))
