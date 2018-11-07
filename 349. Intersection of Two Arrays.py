"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.
"""


class Solution(object):
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))


class Solution(object):
    def intersection(self, nums1, nums2):
        res = []
        for n in nums1:
            if n not in res and n in nums2:
                res.append(n)
        return res 


class Solution(object):
    def intersection(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        res = set()
        if m >= n:
            for n in nums2:
                if n in nums1:
                    res.add(n)
        else:
            for n in nums1:
                if n in nums2:
                    res.add(n)
        return list(res)
