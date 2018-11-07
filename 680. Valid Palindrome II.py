"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

"""

"""
https://www.youtube.com/watch?v=hvI-rJyG4ik
"""

class Solution(object):
    def validPalindrome(self, s):
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return self.isPalindrome(s, left+1, right) or
                self.isPalindrome(s, left, right-1)
            else:
                left += 1
                right -= 1
        return True



    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:                         #注意：这个else一定要写，否则会造成错误！！
                return False
        return True






#超时！！
class Solution(object):
    def validPalindrome(self, s):
           """
        :type s: str
        :rtype: bool
        """
        if self.isPalindrome(s):
            return True
        for i in range(len(s)):
            if self.isPalindrome(s[0:i] + s[i+1:]):
                return True
        return False

    def isPalindrome(self, s):
        li = list(s)
        return li[:] == li[::-1]   #注意：这里很容易犯错，一定是==用于比较！！
