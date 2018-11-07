"""
Given an array with n integers, you need to find if there are triplets (i, j, k) which satisfies following conditions:

0 < i, i + 1 < j, j + 1 < k < n - 1
Sum of subarrays (0, i - 1), (i + 1, j - 1), (j + 1, k - 1) and (k + 1, n - 1) should be equal.
where we define that subarray (L, R) represents a slice of the original array starting from the element indexed L to the element indexed R.
Example:
Input: [1,2,1,2,1,2,1]
Output: True
Explanation:
i = 1, j = 3, k = 5.
sum(0, i - 1) = sum(0, 0) = 1
sum(i + 1, j - 1) = sum(2, 2) = 1
sum(j + 1, k - 1) = sum(4, 4) = 1
sum(k + 1, n - 1) = sum(6, 6) = 1
Note:
1 <= n <= 2000.
Elements in the given array will be in range [-1,000,000, 1,000,000].

"""

"""
思路：拆出的两段和相等，则把这个相等的值加入一个集合中，然后再遍历k的所有情况，同样遍历所有的拆分情况，如果拆出两段和相等，再看这个相等的和是否在集合中，
如果存在，说明拆出的四段和都可以相同，那么返回true即可，否则当遍历结束了，返回false。
O(N^2)
"""

class Solution(object):
    def splitArray(self, nums):
        n = len(nums)
        sums = [0] * n
        sums[0] = nums[0]
        if n < 7:
            return False

        for i in range(1, n):
            sums[i] = sums[i-1] + nums[i]

        for j in range(3, n-3):
            s = set()
            for i in range(1, j-1):
                if sums[i-1] == (sums[j-1] - sums[i]):
                    s.add(sums[i-1])

            for k in range(j+2, n-1):
                s3 = sums[k-1] - sums[j]
                s4 = sums[n-1] - sums[k]
                if s3 == s4 and s3 in s:
                    return True
        return False



#Brutal Force 超时！！
class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        for i in range(n):
            for j in range(i+2, n):
                for k in range(k+2,n-1):
                    if sum(list[0:i]) == sum(list[i+1:j]) == sum(list[k+1, n]):
                        return True
        return False
