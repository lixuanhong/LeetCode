"""Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome."""

def isPalindrome(x):
    if x < 0:
        return False
    res = 0
    temp = x
    while x:
        res = res * 10 + x % 10
        x = x // 10
    if temp == res:
        return True
    else:
        return False

print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(10))
