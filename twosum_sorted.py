"""Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.
Note:
Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice."""

# Best - Dictionary - O(n) ~ n
def twoSum(nums, target):
    look_up = {}
    for i, v in enumerate(nums):
        if target - v in look_up:
            return [look_up[target-v]+1, i+1]
        look_up[v] = i
    return "No two sum solution"

numbers = [2,7,11,15]
print(twoSum(numbers, 9))

# Binary Search - O(n) ~ nlog(n)
def twoSum(nums, target):
    for i in range(len(nums)):
        x = target - nums[i]
        start = i + 1
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) //2 # // floor division results into whole number adjusted to the left (integer division)
            if nums[mid] == x:
                return [i+1, mid+1]
                break
            elif nums[mid] > x:
                end = mid - 1
            elif nums[mid] < x:
                start = mid + 1
    return "No two sum solution"

numbers = [2,4,5,6,7,11,15,16]
print(twoSum(numbers, 9))
