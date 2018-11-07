"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = tmp = head
        while tmp.next:
            while tmp.val == tmp.next.val:
                if tmp.next.next:
                    tmp.next = tmp.next.next
                else:
                    tmp.next = None
                    return dummy.next
            tmp = tmp.next
        return dummy.next
