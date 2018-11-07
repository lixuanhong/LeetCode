"""
Some people will make friend requests. The list of their ages is given and ages[i] is the age of the ith person.

Person A will NOT friend request person B (B != A) if any of the following conditions are true:

age[B] <= 0.5 * age[A] + 7
age[B] > age[A]
age[B] > 100 && age[A] < 100
Otherwise, A will friend request B.

Note that if A requests B, B does not necessarily request A.  Also, people will not friend request themselves.

How many total friend requests are made?

Example 1:

Input: [16,16]
Output: 2
Explanation: 2 people friend request each other.
Example 2:

Input: [16,17,18]
Output: 2
Explanation: Friend requests are made 17 -> 16, 18 -> 17.
Example 3:

Input: [20,30,100,110,120]
Output:
Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.


Notes:

1 <= ages.length <= 20000.
1 <= ages[i] <= 120.
"""

"""
思路：首先题目中的B > A时A不会发送说明了一个人只能向年龄小于等于自己的人发送，由此可以先对数组进行排序，然后进行查找。

还有一个可以借鉴的就是同龄人发送的个数是一样的，可以记录在数组或者HashMap中，以便重用。
"""

import collections
class Solution(object):
    def numFriendRequests(self, ages):
        counter = collections.Counter(ages)
        res = 0
        for age in ages:
            counter[age] -= 1     #不能和自己交朋友
            left, right = age/2 + 8, age   #在这个区间的人都可以发request
            res += sum(counter[age] for age in range(left, right+1))
            counter[age] += 1  #要把自己补充回counter
        return res



# 用dict()还是超时，java可以通过
class Solution(object):
    def numFriendRequests(self, ages):
        if ages is None or len(ages) <= 1:
            return 0
        dict = {}
        res = 0
        ages.sort()
        for i in range(len(ages)):
            if ages[i] in dict.keys():
                res += dict.get(ages[i])
                continue
            sum = 0
            for j in range(len(ages)):
                if j! = i and self.request(ages[i],ages[j]):
                    sum += 1
            dict[ages[i]] = sum
            res += sum
        return res

    def request(self, A, B):
        if B <= 0.5 * A + 7:
            return False
        elif B > A:
            return False
        elif B > 100 and A < 100:
            return False
        else:
            return True




# Time Limit Exceed
class Solution(object):
    def numFriendRequests(self, ages):
        ages.sort()
        sum = 0
        for i in range(len(ages)):
            for j in range(i+1, len(ages)):
                if ages[i] == ages[j]:
                    if ages[i] <= 14:
                        continue
                    sum += 2
                elif ages[i] > 0.5 * ages[j] + 7:
                    sum += 1
        return sum



# Time Limit Exceed
class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        sum = 0
        if len(ages) <= 1:
            return 0
        for i in range(len(ages)):
            for j in range(i+1, len(ages)):
                if ages[j] > ages[i]:
                    continue
                elif ages[j] <= 0.5 * ages[i] + 7:
                    continue
                elif ages[j] > 100 and ages[i] < 100:
                    continue
                else:
                    sum += 1

        for i in in range(len(ages)):
            for j in range(i+1, len(ages)):
                if ages[i] > ages[j]:
                    continue
                elif ages[i] <= 0.5 * ages[j] + 7:
                    continue
                elif ages[i] > 100 and ages[j] < 100:
                    continue
                else:
                    sum += 1

        return sum
