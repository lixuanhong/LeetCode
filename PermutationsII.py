"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""
# A little improvement
class Solution:
    def permuteUnique(self, nums):
        def helper(nums, used, tmp, ans):
            if len(nums) == 0: return []
            if len(tmp) == len(nums):
                ans.append(list(tmp))           #一定要注意是list的shallow copy!!

            for i in range(len(nums)):
                if used[i] == True: continue    #数组有重复值得情况下，对每个取值元素标记一下，就不会取到已经取过的元素; 表示正在遍历
                if i > 0 and nums[i] == nums[i-1] and used[i-1] == False: continue #如果后一个元素和前一个元素相同，并且前一个元素已经遍历，那么跳过;比较nums[i]和nums[i-1]是在对数组已经排序的基础上的
                used[i] = True
                tmp.append(nums[i])
                helper(nums, used, tmp, ans)  #遍历
                tmp.pop()
                used[i] = False

        ans = []
        used = [False] * len(nums)
        nums.sort() #需要对nums进行排序
        helper(nums, used, [], ans)
        return ans





#My Solution - Accepted but slow
class Solution:
    def permuteUnique(self, nums):
        def helper(nums, used, tmp, ans):
            if len(nums) == 0: return []
            if len(tmp) == len(nums):
                if tmp not in ans:             #因为数组有重复值，需要去除重复的序列
                    ans.append(list(tmp))

            for i in range(len(nums)):
                if used[i] == True: continue    #数组有重复值得情况下，对每个取值元素标记一下，就不会取到已经取过的元素
                used[i] = True
                tmp.append(nums[i])
                helper(nums, used, tmp, ans)
                tmp.pop()
                used[i] = False

        ans = []
        used = [False] * len(nums)
        helper(nums, used, [], ans)
        return ans

obj = Solution()
nums = [1,1,2]
print(obj.permuteUnique(nums))
