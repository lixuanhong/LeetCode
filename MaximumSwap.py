"""
Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: 9973
Output: 9973
Explanation: No swap.
Note:
The given number is in the range [0, 108]
"""

"""
思路：
需要交换位置的一定是逆序对。在所有的逆序对里面怎么选择产生最大结果的swap呢？假设数组中的最大元素是a，那么首先看a之前有没有比a小的数，
如果有，则将最前面比a小的数和a交换即可；如果没有，则说明a无法参与交换，这样就再看次大元素b，采用和a同样的处理方法类推即可。

如果我们从后往前扫描，则只需要进行一遍扫描：我们记录一个截止当前的最大值和其对应位置，再记录一下当前参与交换的两个数的值和对应位置。
扫描的过程中，如果遇到比最大值还大的数出现，则更新最大值及其对应位置；否则如果发现当前数比截止当前的最大值小，那么就更新swap为当前数和当前最大数之间的swap。
这样最终结果就是最佳的swap。算法的空间复杂度是O(n)，时间复杂度也是O(n)。
"""

class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        A = list(map(int,str(num)))
        max_num, max_idx = -1, -1
        left_idx, right_idx = -1, -1
        for i in range(len(A)-1, -1, -1):
            if A[i] > max_num:
                max_num = A[i]
                max_idx = i
                continue
            if A[i] < max_num:
                left_idx = i
                right_idx = max_idx
        if left_idx == -1:
            return num
        A[left_idx], A[right_idx] = A[right_idx], A[left_idx]
        return int("".join(str(i) for i in A))
