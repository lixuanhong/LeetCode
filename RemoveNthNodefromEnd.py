"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# My Solution
class Solution(object):
    def removeNthFromEnd(self, head, n):
        if not head:
            return None
        tmp, len = head, 0
        while tmp:
            len += 1
            tmp = tmp.next
        start, end = 0, len - n + 1
        pre = ListNode(0)
        pre.next = head
        cur = head
        if start == end - 1:
            pre.next = cur.next
            return pre.next
        while start < end - 1:
            start += 1
            pre = cur
            cur = cur.next
        cur = cur.next
        pre.next = cur
        return head








class Solution(object):
    def removeNthFromEnd(self, head, n):
        tmp = slow = ListNode(0)
        tmp.next = head
        fast = head
        length = self.length(head)
        for i in range(1, length - n + 2):
            if i == 1:
                fast = fast.next
            else:
                fast = fast.next
                slow = slow.next
        slow.next = fast
        return tmp.next


    def length(self, head):
        i = 0
        while(head != None):
            i += 1
            head = head.next
        return i
