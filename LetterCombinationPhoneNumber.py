"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
"""

"""
思路：标准的DFS+backtracking
Time Complexity O(4^n), n is the length of the Input
Space Complexity O(4^n + n)
"""
class Solution(object):
    def letterCombinations(digits):
        dict = {'2':['a', 'b', 'c'], '3':['d', 'e', 'f'], '4':['g', 'h', 'i'],
                '5':['j', 'k', 'l'], '6':['m', 'n', 'o'], '7':['p', 'q', 'r', 's'],
                '8':['t', 'u', 'v'], '9':['w','x', 'y', 'z']}

        n = len(digits)
        if n == 0:
            return []
        cur, res = "", []
        self.dfs(digits, dict, 0, cur, res)
        return res

    def dfs(self, digits, dict, l, cur, res):
        if l == len(digits):
            res.append(cur)
            return

        for c in dict[digits[l]]:
            cur += c
            self.dfs(digits, dict, l+1, cur, res)
            cur = cur[:-1]
