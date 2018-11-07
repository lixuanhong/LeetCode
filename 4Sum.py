"""Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.

Note:
The solution set must not contain duplicate quadruplets."""

def fourSum(nums, target):
    res, dict = set(), {}
    if len(nums) < 4: return []
    nums.sort()                              #为什么需要排序？非常重要！因为这个nums里面存在重复元素
    for p in range(len(nums)-1):
        for q in range(p+1, len(nums)):
            if nums[p] + nums[q] not in dict:     #保证值和坐标都是从小到大排列
                dict[nums[p] + nums[q]] = [(p, q)]
            else:
                dict[nums[p] + nums[q]].append((p, q))

    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            T = target - nums[i] - nums[j]
            if T in dict:
                for k in dict[T]:
                    if k[0] > j:             #这里保证不要取到重复的元素，坐标是唯一的
                        res.add((nums[i], nums[j], nums[k[0]], nums[k[1]]))
    return [list(i) for i in res]


nums = [1, 0, -1, 0, -2, 2]
target = 0
print(fourSum(nums, 0))

"""解题思路：一开始想要像3Sum那样去解题，时间复杂度为O(N^3)，可无论怎么写都是Time Limited Exceeded。而同样的算法使用C++是可以通过的。说明Python的执行速度比C++慢很多。
还说明了一点，大概出题人的意思不是要让我们去像3Sum那样去解题，否则这道题就出的没有意义了。这里参考了kitt的解法：http://chaoren.is-programmer.com/posts/45308.html

需要用到哈希表的思路，这样可以空间换时间，以增加空间复杂度的代价来降低时间复杂度。首先建立一个字典dict，字典的key值为数组中每两个元素的和，每个key对应的value为这两个元素的下标组成的元组，
元组不一定是唯一的。如对于num=[1,2,3,2]来说，dict={3:[(0,1),(0,3)], 4:[(0,2),(1,3)], 5:[(1,2),(2,3)]}。这样就可以检查target-key这个值在不在dict的key值中，
如果target-key在dict中并且下标符合要求，那么就找到了这样的一组解。由于需要去重，这里选用set()类型的数据结构，即无序无重复元素集。最后将每个找出来的解(set()类型)转换成list类型输出即可。"""

"""set.add(x) Method: Adds the item x to set if it is not already present in the set."""
