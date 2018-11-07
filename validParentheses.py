"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. 审题：这个字符串只包括括号元素！！！

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

"""

#思路：用栈来操作，将所有的字符依次入栈，当栈顶的括号和正要入栈的括号匹配时将栈顶的括号弹出且不入栈，否则入栈新的括号。最后，只有当栈里没有括号时，才表明输入是有效的。

def isValid(s):
    stack = []
    dict = {')': '(', ']':'[', '}':'{'}
    for i in s:
        if i in dict:
            if stack == [] or dict[i] != stack.pop():
                return False
        else:
            stack.append(i)
    return len(stack) == 0


print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))
print(isValid("([)]"))
print(isValid("{[]}"))
