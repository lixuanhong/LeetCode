"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head):
        if head != None and head.next != None and head.next.next != None:

            #break linked list into two equal length
            slow = fast = head
            while fast != None and fast.next != None: #奇偶数两种情况；奇数终止于最后一个元素，fast.next == none; 偶数终止于倒数第二个元素，下一轮fast == none
                slow = slow.next
                fast = fast.next.next
            head1 = head
            head2 = slow.next
            slow.next = None

            #reverse linked list head2
            p = head2
            q = head2.next
            head2.next = None
            while q:
                r = q.next
                q.next = p
                p = q
                q = r
            head2 = p

            #merge two linked list head1 and head2
            node1 = head1; node2 = head2
            while node2 != None:
                tmp1 = node1.next
                tmp2 = node2.next
                node1.next = node2
                node2.next = tmp1
                node1 = tmp1
                node2 = tmp2

#思路：拆分链表 - 快指针移动速度是慢指针移动速度的2倍，因此当快指针到达链表尾时，慢指针到达中点。
#思路：链表反转 - 使用3个指针遍历单链表，逐个链接点进行反转。 https://blog.csdn.net/feliciafay/article/details/6841115
