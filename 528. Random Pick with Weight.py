"""
Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.
Example 1:

Input:
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]
Example 2:

Input:
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any.
"""

"""
我们首先看如果array只有两个元素该如何实现Random Pick with Weight，假设数组为[3, 5]，那么显然我们应该实现3/8的概率选到3，5/8的概率选到5。那么显而易见的，我们应该生成[1, 8]的随机数，
如果随机数落在[1, 3]我们选3，否则选5。这个思路很容易推广，如果我们计算输入数组的presum数组和总的和sum，我们只需要生成[1, sum]的随机数r，去presum里找大于等于r的最小的数对应的index即可。
weight都是大于0的，presum数组是严格递增的，我们binary search即可。时间复杂度preprocess生成presum数组O(n)，n为输入数组长度，pick的复杂度为O(log n).

做法是把概率分布函数转化为累计概率分布函数。然后通过随机数，进行二分查找。

比如，输入是[1,2,3,4]，那么概率分布是[1/10, 2/10, 3/10, 4/10]，累积概率分布是[1/10, 3/10, 6/10, 10/10].总和是10。如果我们产生一个随机数，在0~9之中，然后判断这个数字在哪个区间中就能得到对应的索引。
各区间的含义是：

[0], [1, 2], [3, 4, 5], [6, 7, 8, 9]

"""

class Solution(object):
    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.sum = 0
        self.nums = []
        for n in w:
            self.sum += n
            self.nums.append(self.sum)


    def pickIndex(self):
        """
        :rtype: int
        """
        total = self.nums[-1]
        rand = random.randint(1, total)   #返回值包括1和total
        left, right = 0, len(self.nums) - 1
        while left < right:
            mid = (left + right) // 2
            if self.nums[mid] > rand:
                right = mid
            elif self.nums[mid] < rand:
                left = mid + 1
            else:
                return mid
        return left
