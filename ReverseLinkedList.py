"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        if not head:
            return None
        pre = None
        cur = next = head
        while cur:
            next = cur.next 
            cur.next = pre
            pre = cur
            cur = next
        head = pre
        return head
