# Brutal Force
# def twoSum(nums, target):
#     try:
#         for i in nums:
#             for j in nums:
#                 value = target - i
#                 if (j == value and j != i):
#                     return [nums.index(i), nums.index(j)]
#     except:
#         return None
#
# nums = [2,8,7,11,15]
# print(twoSum(nums, 9))
#
# Dictionary
# def twoSum(nums, target):
#     look_up = dict((v, i) for i, v in enumerate(nums)) #emunerate returns index and value of iterable {2: 0, 7: 1, 11: 2, 15: 3}
#     for v, i in look_up.items(): # for v in look_up: only return keys
#         complement = target - v
#         if (complement in look_up and look_up.get(complement) != i):
#             return [i, look_up.get(complement)]
#     return "No two sum solution"

# nums = [3,3] # this method doesn't work for same values
# print(twoSum(nums, 6))

# look_up = dict((v, i) for i, v in enumerate(nums))
# print(look_up)
#
# Correct solution
def twoSum(nums, target):                  #这道题提到会存在唯一解，所以不会有重复的数字
    dict = {}
    res = []
    for idx, num in enumerate(nums):
        if target - num in dict:
            return [idx, dict[target-num]]     # dict[target-num]肯定是在idx之后的
        dict[num] = idx                  #因为不会有重复数字，所以直接加入字典！
    return res
