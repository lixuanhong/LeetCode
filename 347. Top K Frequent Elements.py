"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict = {}
        for num in nums:
            if num in dict.keys():
                dict[num] += 1
            else:
                dict[num] = 1

        res = []
        for key, value in dict.items():
            res.append([key, value])
        res.sort(reverse=True, key = lambda x: x[1])
        print(res)

        ans = []
        for i in range(k):
            ans.append(res[i][0])
        return ans
