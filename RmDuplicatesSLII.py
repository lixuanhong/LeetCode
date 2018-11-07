"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head
        dummy = pre = ListNode(0)
        dummy.next = tmp = p = head
        dict = {}
        while tmp and tmp.next:
            if tmp.val == tmp.next.val:
                dict[tmp.val] = 1
                tmp = tmp.next.next
            else:
                tmp = tmp.next

        while p.next:
            if p.val in dict.keys():
                p = p.next
            else:
                pre.next = p
                p = p.next
                pre = pre.next
        return dummy.next
