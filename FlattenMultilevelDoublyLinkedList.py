"""
You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.



Example:

Input:
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL

Output:
1-2-3-7-8-11-12-9-10-4-5-6-NULL


Explanation for the above example:

Given the following multilevel doubly linked list:
"""

"""
思路：如果当前点cur 没有child, 直接跳到cur.next 进行下次计算；如果cur 有child，找到childTail,将childTrail指向cur.next;
然后cur = child继续向下遍历
Time Complexity: O(N)
Space Complexity: O(1)
"""

class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        cur = head
        while cur:
            if not cur.child:
                cur = cur.next
                continue

            child = cur.child
            childTail = child
            while childTail.next:
                childTail = childTail.next

            cur.child = None
            child.prev = cur
            childTail.next = cur.next
            if cur.next:
                cur.next.prev = childTail
            cur.next = child
            cur = cur.next
        return head
