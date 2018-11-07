"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.

Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:

The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.
"""

"""
思路：用segment tree来查找区间值, time complexity O(lgN)
"""

class NumArray(object):
    def __init__(self, nums):                   #construct the segment tree
        self.nums = nums
        n = len(nums)
        if n == 0:
            return None
        self.tree = [0] * 2 * n
        for i in range(n, 2 * n):
            self.tree[i] = self.nums[i - n]
        for i in range(n - 1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i + 1]


    def update(self, i, val):                   #Besides update the child, also update the parent
        i += len(self.nums)                     #the value of the parent equals to the sum of left tree and right tree
        self.tree[i] = val
        while i > 0:
            left = i
            right = i
            if i % 2 == 0:
                right = i + 1
            else:
                left = i - 1
            self.tree[i/2] = self.tree[left] + self.tree[right]
            i /= 2

    def sumRange(self, i, j):
        i += len(self.nums)
        j += len(self.nums)
        sum = 0
        while i <= j:
            if i % 2 != 0:
                sum += self.tree[i]
                i += 1
            if j % 2 != 1:
                sum += self.tree[j]
                j -= 1
            i /= 2
            j /= 2
        return sum
