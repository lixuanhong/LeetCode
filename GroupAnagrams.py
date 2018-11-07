"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""

import collections
class Solution:
    def groupAnagrams(self, strs):
        dict = collections.defaultdict(list)
        for word in strs:
            sortedword = ''.join(sorted(word))
            dict[sortedword].append(word)

        res = []
        for key in dict:
            res.append(dict[key])
        return res

obj = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(obj.groupAnagrams(strs))



"""
sorted(iterable) - returns a sorted list from the given iterable

pyString = 'Python'
print(sorted(pyString)) # ['P', 'h', 'n', 'o', 't', 'y']

# set
pySet = {'e', 'a', 'u', 'o', 'i'}
print(sorted(pySet, reverse=True)) #['u', 'o', 'i', 'e', 'a']
"""
