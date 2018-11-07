"""
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head, val):
        new_head = temp = ListNode(0) #new_head是dummy node, 因为temp一直在变化，最后返回new_head指针
        temp.next = head
        while head:
            if head.val == val:
                temp.next = head.next
            else:
                temp = temp.next
            head = head.next
        return new_head.next #最后返回的是new_head指针
