"""Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value."""
# Haven't been submitted to leetcode due to the lock

# class TwoSum(object):
#     def __init__(self):
#         """initialize your data structure here"""
#         global nums
#         nums = []
#
#     def add(self, number):
#         """Add the number to an internal data structure."""
#         nums.append(number)
#
#     def find(self, value):
#         """Find if there exists any pair of numbers which sum is equal to the valueself.
#            type value: int
#            rtype: bool"""
#         look_up = {}
#         for i, v in enumerate(nums):
#             if (value - v) in look_up:
#                 return True
#             look_up[v] = i
#         return False
#
# twosum = TwoSum()
# twosum.add(1);
# twosum.add(3);
# twosum.add(5);
# print(twosum.find(4)); #True
# print(twosum.find(7)); #False

class TwoSum(object):
    def __init__(self):
        """initialize your data structure here"""
        self.dict = dict()

    def add(self, number):
        """Add the number to an internal data structure."""
        if number not in self.dict:
            self.dict[number] = 1
        else:
            self.dict[number] += 1
        #print(self.dict)

    def find(self, value):
        """Find if there exists any pair of numbers which sum is equal to the valueself.
           type value: int
           rtype: bool"""
        for num in self.dict:
            if value - num in self.dict and (value - num != num or dict[num] > 1):
                return True
        return False

twosum = TwoSum()
twosum.add(1); # {1: 1}
twosum.add(3); # {1: 1, 3: 1}
twosum.add(5); # {1: 1, 3: 1, 5: 1}
twosum.add(3); # {1: 1, 3: 2, 5: 1}
print(twosum.find(4));
print(twosum.find(6));

数据结构：dictionary
