"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
"""

class Solution(object):
    def strStr(self, haystack, needle):
        if needle == "": return 0
        if needle in haystack:
           return haystack.index(needle)
        else:
            return -1

obj = Solution()
haystack = "hello"
needle = "ll"
print(obj.strStr(haystack, needle))

#str.index(str, beg=0 end = len(string))
#It determines if string str occurs in string or in a substring of string if starting index beg and ending index end are given.
#IThis method is same as find(), but raises an exception if sub is not found.
