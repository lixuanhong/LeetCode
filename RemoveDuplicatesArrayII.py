"""
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,1,2,3,3],

Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}

"""

#解题思路：一种巧妙的解法。使用两个指针prev和curr，判断A[curr]是否和A[prev]、A[prev-1]相等，如果相等curr指针继续向后遍历，
#直到不相等时，将curr指针指向的值赋值给A[prev+1]，这样多余的数就都被后面的数覆盖了。最后prev+1值就是数组的长度。

class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) <= 2: return len(nums)
        prev = 1; curr = 2
        while curr < len(nums):
            if nums[curr] == nums[prev] and nums[curr] == nums[prev-1]:
                curr += 1
            else:
                prev += 1
                nums[prev] = nums[curr]
                curr += 1
            return prev + 1
