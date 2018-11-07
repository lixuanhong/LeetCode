"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is not None:
            return l2
        if l2 is None and l1 is not None:
            return l1
        if l1 is None and l2 is None:
            return None
        s1, s2 = 0, 0
        head1, head2 = l1, l2
        while head1:
            s1 = s1 * 10 + head1.val
            head1 = head1.next
        while head2:
            s2 = s2 * 10 + head2.val
            head2 = head2.next
        s = s1 + s2
        head = l = ListNode(0)
        for n in str(s):
            head.next = ListNode(int(n))
            head = head.next
        return l.next
