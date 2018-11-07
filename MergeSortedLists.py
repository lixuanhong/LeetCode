"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1 and l2:
            return l2
        if not l2 and l1:
            return l1
        if not l1 and not l2:
            return None

        head = ListNode(0)
        l = head
        while l1 and l2:
            if l1.val <= l2.val:
                l.next = l1
                l1 = l1.next
                l = l.next
            else:
                l.next = l2
                l2 = l2.next
                l = l.next
        if l1 == None:
            l.next = l2
        else:
            l.next = l1
        return head.next
