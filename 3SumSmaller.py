"""Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

For example, given nums = [-2, 0, 1, 3], and target = 2.

Return 2. Because there are two triplets which sums are less than 2:

[-2, 0, 1]
[-2, 0, 3]
Follow up:
Could you solve it in O(n2) runtime?"""

# Solution from website
# def threeSumSmaller(nums, target):
#     nums.sort()
#     count = 0
#     for i in range(len(nums) - 2):
#         if i > 0 and nums[i] == nums[i-1]: continue
#         j = i + 1
#         k = len(nums) - 1
#         while (j < k):
#             sum = nums[i] + nums[j] + nums[k]
#             if sum < target:
#                 count = count + (k - j)  #这种解法有问题，没有考虑重复解，测试nums = [-2, 0, 0, 1, 3]结果有误
#                 j = j + 1
#             else:
#                 k = k - 1
#     return count
#
# nums = [-2, 0, 0, 1, 3]
# print(threeSumSmaller(nums, 2))

#My Solution - haven't been submitted to Leetcode due to version limit 需要提交验证该解法是否正确
def threeSumSmaller(nums, target):
    nums.sort()
    list = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]: continue
        j = i + 1
        k = len(nums) - 1
        while (j < k):
            sum = nums[i] + nums[j] + nums[k]
            if sum < target:
                list.append([nums[i], nums[j], nums[k]])
                if k > j + 1:
                    k = k - 1
                    while j < k and nums[k] == nums[k+1]:
                        k = k - 1
                else: # k == j+1
                    j = j + 1
                    k = len(nums) - 1
                    while j < k and nums[j] == nums[j-1]:
                        j = j + 1
            else:
                if k > j + 1:
                    k = k - 1
                    while j < k and nums[k] == nums[k+1]:
                        k = k - 1
                else: # k == j+1
                    break
    #return list  #[[-2, 0, 3], [-2, 0, 1], [-2, 0, 0], [0, 0, 1]]
    return len(list)



nums = [-2, 0, 0, 1, 3]
print(threeSumSmaller(nums, 2))
