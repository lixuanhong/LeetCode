"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.
"""

"""
思路：https://www.youtube.com/watch?v=ABMLLVzf4ZQ
Time Complexity O(n)
Space Complexity O(n)
"""

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        pre_op = "+"
        num = 0
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if s[i] in "+-*/" or i == len(s) - 1:
                if pre_op == "+":
                    stack.append(num)
                if pre_op == "-":
                    stack.append(-num)
                if pre_op == "*":
                    stack.append(stack.pop()*int(s[i]))
                if pre_op == "/":
                    top = stack.pop()
                    if top < 0:
                        stack.append(- (-top // num))     #注意：-5/2 => -3 in python
                    else:
                        stack.append(top // num)
                pre_op = s[i]
                num = 0

        res = 0
        for i in range(len(stack)):
            res += stack[i]
        return res
