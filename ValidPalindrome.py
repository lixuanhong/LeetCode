"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false

"""

class Solution:
    def isPalindrome(self, s):
        list = []
        for c in s:
            if c.isalnum():   #checks whether the string consists of alphanumeric characters
                list.append(c.lower())
        return list == list[::-1] #list[::-1]是list的reverse

#No extra space
class Solution:
    def isPalindrome(self, s):
        s = ''.join(e for e in s if e.isalnum()).lower()
        return s == s[::-1]


#Another writing
class Solution:
    def isPalindrome(self, s):
        list = []
        for c in s:
            if c.isalnum():
                list.append(c.lower())

        for i in range(len(list)//2):
            if list[i] != list[len(list) -1 - i]:
                return False
        return True

#Another one - no need to create a new list
class Solution:
    def isPalindrome(self, s):
        i = -1
        j = len(s)
        while True:
            i += 1
            j -= 1
            if i >= j:
                return True
            while i < j:
                if not s[i].isalnum():
                    i += 1
                else:
                    break
            while i < j:
                if not s[j].isalnum():
                    j -= 1
                else:
                    break
            if s[i].lower() != s[j].lower():
                return False


obj = Solution()
s = "Race a car"
print(obj.isPalindrome(s))
