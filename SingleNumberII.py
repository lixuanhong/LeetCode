"""
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99
"""
#考察位操作
class Solution:
    def singleNumber(self, nums):
        one = 0; two = 0; three = 0;
        for i in range(len(nums)):
            two |= nums[i] & one  #two为1时，不管nums[i]是什么，two都是1
            one = nums[i] ^ one   #异或操作，都是1就进位
            three = ~(one & two)  #后面三步意思：如果one和two都为1时，就清0，反之就保持原来的状态
            one &= three
            two &= three
        return one

"""
& 与 - 两位都为1，结果为1
| 或 - 有一位为1，结果为1
~ 非 - ~0 = 1，~1 = 0
^ 异或 - 两位不相同，结果为1
"""




import collections
class Solution:
    def singleNumber(self, nums):
        dict = collections.Counter(nums)
        return min(dict, key=dict.get) #get the maxmium or minimum value from a dictionary

obj = Solution()
nums = [0,1,0,1,0,1,99]
print(obj.singleNumber(nums))
