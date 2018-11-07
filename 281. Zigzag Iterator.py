"""
Given two 1d vectors, implement an iterator to return their elements alternately.

Example:

Input:
v1 = [1,2]
v2 = [3,4,5,6]

Output: [1,3,2,4,5,6]

Explanation: By calling next repeatedly until hasNext returns false,
             the order of elements returned by next should be: [1,3,2,4,5,6].
Follow up: What if you are given k 1d vectors? How well can your code be extended to such cases?

Clarification for the follow up question:
The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For example:

Input:
[1,2,3]
[4,5,6,7]
[8,9]

Output: [1,4,8,2,5,9,3,6,7].
"""

#O(1) Space Solution

class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.queue = collections.deque([v for v in (v1, v2) if v])


    def next(self):
        """
        :rtype: int
        """
        v = self.queue.popleft()  #popleft()是deque里面的方法
        res = v.pop(0)  #注意：这里v是一个list,没有popleft()方法，用pop(0)
        if v:
            self.queue.append(v)
        return res


    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.queue) != 0
