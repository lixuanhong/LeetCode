""" Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Note:
The solution set must not contain duplicate triplets. """

# Accepted Solution
def threeSum(nums):
    list = []
    nums.sort() #Sorted array can save a lot of time ~O(nlgn)
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]: #skip the repeat and continue the loop
            continue
        j = i + 1
        k = len(nums) - 1
        while j < k:
            temp = nums[i] + nums[j] + nums[k]
            if temp > 0:
                k = k - 1
            elif temp < 0:
                j = j + 1
            else:
                result.append([nums[i], nums[j], nums[k]])
                j, k = j + 1, k - 1
                while j<k and nums[j]==nums[j-1]:
                    j = j + 1
                while j<k and nums[k]==nums[k+1]:
                    k = k - 1
    return list


nums = [0, 0, 0, 0, 0, 0]
print(threeSum(nums))

#解题逻辑：每进行下一步之前，都要去掉重复，非常重要！顺序稍微调整，运行时间会超时。sort(), 左右两个指针


#My solution 超时
class Solution(object):
    def threeSum(self, nums):
        res = set()
        nums.sort()
        for i in range(len(nums) - 2):
            for j in range(i+1, len(nums) - 1):
                target = -nums[i] - nums[j]
                if target in nums[j+1:]:
                    res.add((nums[i], nums[j], -nums[i]-nums[j]))
        return list(res)
