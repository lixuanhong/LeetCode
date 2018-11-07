"""Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers. You may assume that each input would have exactly one solution."""

def threeSumCloest(nums, target):
    nums.sort()
    diff_min = 1000
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]: continue
        j = i + 1
        k = len(nums) - 1
        while j < k:
            sum = nums[i] + nums[j] + nums[k]
            diff = abs(sum - target)
            if diff < diff_min:
                diff_min = diff
                result = sum
            if sum == target:
                return sum
            elif sum < target:
               j = j + 1
               while j < k and nums[j] == nums[j-1]:
                   j = j + 1
            else:
                k = k - 1
                while j < k and nums[k] == nums[k+1]:
                    k = k - 1
    return result

nums = [1, 1, 1, 0]
print(threeSumCloest(nums, -100))
#关键点：sort(), abs, sum和target比较，左右两个指针
