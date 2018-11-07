"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4

"""

"""
思路：快速选择 Quick Select => Quick Sort的一个部分
跟快速排序一个思路。先取一个枢纽值，将数组中小于枢纽值的放在左边，大于枢纽值的放在右边，具体方法是用左右两个指针，
如果他们小于枢纽值则将他们换到对面，一轮过后记得将枢纽值赋回分界点。如果这个分界点是k，说明分界点的数就是第k个数。
否则，如果分界点大于k，则在左半边做同样的搜索。如果分界点小于k，则在右半边做同样的搜索。

partition函数的k是k-1，因为我们下标从0开始的，我们要比较k和下标，来确定是否左半部分有k个数字。
互换左右时，也要先判断left <= right

时间 Avg O(N) Worst O(N^2) 空间 O(1)
https://www.youtube.com/watch?v=ow04KXJ0kG4 非常重要的题！
"""

#Quick Sort - O(N)
class Solution(object):
    def findKthLargest(self, nums, k):
        if not nums or len(nums) == 0: return None

        left, right = 0, len(nums) - 1

        while True:                                       #这里有个循环控制，要反复的调用partition函数，寻找分隔点
            pos = self.partition(nums, left, right)
            if pos + 1 == k:
                return nums[pos]
            elif pos + 1 < k:
                left = pos + 1
            else:
                right = pos - 1

# 3,2,1,5,6,4 k=3
# pivot: 3 [3,2,1,5,6,4]
# [3,4,6,5,1,2] 3
# pivot: 5 [5,4,6,3,1,2]
# [6,5,4,3,1,2] 4
# [6,5,4,3,1,2] =>4

    def partition(self, nums, left, right):
        pivot = nums[left]
        l = left + 1
        r = right
        while l <= r:
            if nums[l] < pivot and nums[r] > pivot:
                self.swap(nums, l, r)
                l += 1
                r -= 1
            elif nums[l] >= pivot:                  #注意：这里要包含等于，容易写错
                l += 1
            elif nums[r] <= pivot:
                r -= 1
        self.swap(nums, left, r)
        return r



    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

# O(NlgN)
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums or len(nums) == 0: return 0
        nums.sort(reverse=True)
        return nums[k-1]
