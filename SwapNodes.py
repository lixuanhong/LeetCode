"""
Given a linked list, swap every two adjacent nodes and return its head.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
Note:

Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes, only nodes itself may be changed.
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        if head == None or head.next == None:
            return head
        dummy = p = ListNode(0)
        dummy.next = tmp = head

        while tmp and tmp.next:
            p.next = tmp.next
            tmp.next = tmp.next.next
            p.next.next = tmp
            p = p.next.next
            tmp = tmp.next
        return dummy.next

#思路：https://www.youtube.com/watch?v=f45_eF1gmn8
