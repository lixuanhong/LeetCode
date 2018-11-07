"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
"""

"""
思路：转换成二进制
https://www.youtube.com/watch?v=RNaO23ETjhM
"""

class Solution(object):
    def hammingDistance(self, x, y):
        res = 0
        for i in range(31):
            bx = x%2
            by = y%2
            if bx != by:
                res += 1
            x = x/2
            y = y/2
        return res
