"""
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer k and an integer array nums, which contains initial elements from the stream. For each call to the method KthLargest.add, return the element representing the kth largest element in the stream.

Example:

int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
Note:
You may assume that nums' length ≥ k-1 and k ≥ 1.
"""

class KthLargest(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.nums = nums
        self.nums.sort(reverse=True)
        self.k = k


    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        left, right = 0, len(self.nums) - 1
        pos = 0
        while left <= right:                       #因为没有判断数组的长度>=2, 这里用left <= right
            mid = (left + right) // 2
            if self.nums[mid] > val:
                left = mid + 1
            elif self.nums[mid] < val:
                right = mid - 1                    #每次check后，left和right值一定要变化，否则如果数组长度为1会一直进入死循环
            else:
                pos = mid
                self.nums.insert(pos, val)
                return self.nums[self.k - 1]
        pos = left
        self.nums.insert(pos, val)
        return self.nums[self.k - 1]








#超时！！！
class KthLargest(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.nums = nums
        self.k = k


    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.nums.append(val)
        self.nums.sort(reverse=True)
        return self.nums[self.k-1]
