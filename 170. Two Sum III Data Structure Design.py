"""
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

Example 1:

add(1); add(3); add(5);
find(4) -> true
find(7) -> false
Example 2:

add(3); add(1); add(2);
find(3) -> true
find(6) -> false
"""

class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}


    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        if number in dict:
            self.dict[number] += 1        #注意：公式里面用global变量一定要加self, 很容易犯错！！
        else:
            self.dict[number] = 1


    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for key, val in self.dict.items():
            if value - key in self.dict():
                if value - key != key:
                    return True
                else:
                    if val >= 2:
                        return True
        return False



#超时
class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []
        self.dict = {}


    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """

        for n in list:
            if number + n not in dict:
                dict[number+n] = True

        if number not in list:
            list.append(number)


    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        if value in dict:
            return True
        else:
            return False
