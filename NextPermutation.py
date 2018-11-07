"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

"""

"""
解题思路：输出字典序中的下一个排列。比如123生成的全排列是：123，132，213，231，312，321。那么321的next permutation是123。
下面这种算法据说是STL中的经典算法。在当前序列中，从尾端往前寻找两个相邻升序元素，升序元素对中的前一个标记为partition。
然后再从尾端寻找另一个大于partition的元素，并与partition指向的元素交换，然后将partition后的元素（不包括partition指向的元素）逆序排列。
比如14532，那么升序对为45，partition指向4，由于partition之后除了5没有比4大的数，所以45交换为54，即15432，然后将partition之后的元素逆序排列，
即432排列为234，则最后输出的next permutation为15234。确实很巧妙。
"""

class Solution(object):
    def nextPermutation(self, nums):
        if len(nums) <=1: return nums
        partition = -1
        for i in range(len(nums)-2, -1, -1): #range(start, stop, step) stop - generate the number upto but not including this number
            if nums[i] < nums[i+1]:   #说明partition后面的元素都是从大到小的
                partition = i
                break
        if partition == -1:
            nums.reverse() #整个list被逆序排序
            #return nums 不用return, 因为nums已经被in-place改变
        else:
            for i in range(len(nums) - 1, partition, -1):
                if nums[i] > nums[partition]:
                    nums[i], nums[partition] = nums[partition], nums[i]
                    break
            nums[partition+1:len(nums)] = nums[partition+1:len(nums)][::-1] #partition后面list被逆序排序，即从小到大 #list slicing list[start:end] end - generate the number upto but not including this number
            #return nums

"""
values = [100, 200, 300, 400, 500]
# Slice from start to second index.
slice = values[:2]
print(slice) # [100:200]
"""
