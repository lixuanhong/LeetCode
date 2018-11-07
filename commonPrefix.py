"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""


#遍历每一个字符串，用指针对应的字符与基准中相应的字符比较，如不同则前面的子字符串就是所要求的结果；
#如果全都相同，则指针右移。还有一种情况要考虑，后面的字符串可能没有第一个字符串长，如果指针超过了最短的字符串也应该终止。
def longestCommonPrefix(strs):
    if not strs:
        return ""
    for i in range(len(strs[0])):
        for str in strs:
            if len(str) <= i or strs[0][i] != str[i]:
                return strs[0][:i]
    return strs[0]

print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))


Another solution - using python zip
def longestCommonPrefix(strs):
    result = ""
    for n in zip(*strs):
        if len(set(n)) == 1:
            result += n[0]
        else:
            return result
    return result

"""
s = ["flower","flow","flight"]
res = zip(*s)
for item in res:
    print(set(item))

{'f'}
{'l'}
{'o', 'i'}
{'w', 'g'}

"""
