"""
Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n), your function should minimize the number of calls to knows.

Note: There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.

"""

# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):
"""
高频
https://www.youtube.com/watch?v=QDehNYXlCAg
Optimized Solution O(n)

knows(i, j)
By comparing a pair(i,j), we are able to discard one of them

if knows(i,j)
    i is guaranteed not to be celebrity
else
    j is not a celebrity
"""

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1: return -1

        candidate = 0
        for i in range(1, n):                  #最关键点，是这个O(N)的循环； if knows(i, j): i is not a celebrity; else j is not a celebrity
            if knows(candidate, i):
                candidate = i

        for i in range(n):                    #再进行一个for循环，判断元素是否认识candidate && candidate是否认识该元素！！
            if candidate == i:
                continue
            if not knows(i, candidate) or knows(candidate, i):   #注意，python里面不能用！，用not
                return -1
        return candidate