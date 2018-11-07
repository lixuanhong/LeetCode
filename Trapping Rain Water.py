"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
"""

"""
思路：。开辟一个数组leftmosthigh，leftmosthigh[i]为A[i]之前的最高的bar值，然后从后面开始遍历，用rightmax来记录从后向前遍历遇到的最大bar值，那么min(leftmosthigh[i],
 rightmax)-A[i]就是在第i个bar可以储存的水量。例如当i=9时，此时leftmosthigh[9]=3,而rightmax=2，则储水量为2-1=1，依次类推即可。这种方法还是很巧妙的。时间复杂度为O(N)。
"""

class Solution：
    def trap(self, height):
        if len(height) == 0 or height is None:
            return 0
        leftmosthigh = [0] * len(height)
        leftmax = 0
        for i in range(len(height)):
            if height[i] > leftmax:
                leftmax = height[i]
            leftmosthigh[i] = leftmax
        sum = 0
        rightmax = 0
        for i in range(len(height) - 1, -1, -1):
            if height[i] > rightmax:
                rightmax = height[i]
            sum += min(leftmosthigh[i], rightmax) - height[i]
        return sum
