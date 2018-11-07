"""
Solve a given equation and return the value of x in the form of string "x=#value". The equation contains only '+', '-' operation, the variable x and its coefficient.

If there is no solution for the equation, return "No solution".

If there are infinite solutions for the equation, return "Infinite solutions".

If there is exactly one solution for the equation, we ensure that the value of x is an integer.

Example 1:
Input: "x+5-3+x=6+x-2"
Output: "x=2"
Example 2:
Input: "x=x"
Output: "Infinite solutions"
Example 3:
Input: "2x=x"
Output: "x=0"
Example 4:
Input: "2x+3x-6x=x+2"
Output: "x=-1"
Example 5:
Input: "x=x+2"
Output: "No solution"
"""

"""
思路：用'='将等式分为左右两半，分别求左右两侧x的系数和常数值，记为lx, lc, rx, rc，分别求左右两侧x的系数和常数值，记为lx, lc, rx, rc
若x != 0，则x = c / x；否则，若c != 0，说明方程无解；否则，说明有无数组解。

"""

class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        left,right = equation.split("=")
        lx, lc = self.solve(left)
        rx, rc = self.solve(right)
        x, c = lx - rx, rc - lc
        if x:
            return "x=%d" % (c/x)
        elif c:
            return "No solution"
        return "Infinite solutions"

    def solve(self, expression):
        x, c = 0, 0
        num, sign = '', 1
        for char in expression + "#":       #要多一位出来，让最后一个数字或者x被加上！！
            if “0” <= char <= “9”:          #比较字符的ASCII码，不能用int()，因为有的字符不是数字
                num += char
            elif char == "x":
                x += int(num or '1') * sign
                num, sign = '', 1
            else:
                c += int(num or '0') * sign
                num, sign = '', 1
                if char == "-":
                    sign = -1
        return x, c
