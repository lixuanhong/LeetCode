"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""
#题目大意：把单链表中第m-n个元素进行翻转

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        if head == None or head.next == None:
            return head
        dummy = ListNode(0); dummy.next = head
        pre = dummy; cur = head

        for i in range(m-1):
            cur = cur.next
            pre = pre.next

        tmp = ListNode(0)
        for i in range(n - m):
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = pre.next
            pre.next = tmp
        return dummy.next
