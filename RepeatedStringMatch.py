"""
Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.
"""

"""
思路：都是每次给t增加一个字符串A，我们其实可以直接算出最多需要增加的个数，即B的长度除以A的长度再加上2，当B小于A的时候，那么可能需要两个A，所以i就是小于等于2，这样我们每次在t中找B，
如果找到了，就返回i，没找到，就增加一个A，循环推出后返回-1即可。
"""

class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        size_a, size_b = len(A), len(B)
        count = size_b//size_a + 2
        for i in range(1, count+1):
            if B in A * i:
                return i
        return -1
