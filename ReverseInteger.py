"""Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21"""

def reverse(x):
    result = 0
    sign = 1
    if x < 0:
        sign = -1
        x = x * sign
    while x:
        result = result * 10 + x % 10
        x = x // 10

    return result * sign if -2 ** 31 <= result <= 2 ** 31 else 0

print(reverse(123))
print(reverse(-123))
print(reverse(120))
