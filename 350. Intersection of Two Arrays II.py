"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

"""

class Solution(object):
    def intersect(self, nums1, nums2):
        res = []
        for i in nums1:
            if i in nums2:
                res.append(i)
                nums2.remove(i)
        return res

#follow up 将数组排序后用二分查找
class Solution(object):
    def intersect(self, nums1, nums2):
        res = []
        nums2.sort()
        for k in nums1:
            status, j = self.binarySearch(nums2, k)
            if status:
                res.append(k)
                del nums2[j]
        return res


    def binarySearch(self, nums, k):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)/2
            if nums[mid] == k:
                return True, mid
            if nums[mid] < k:
                left = mid + 1
            else:
                right = mid - 1
        return False, 0
