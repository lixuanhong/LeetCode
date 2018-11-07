"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

#思路：难度较低，主要考察链表操作和加法进位的基础知识
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# My Solution
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur1, cur2 = l1, l2
        sum1, sum2 = 0, 0
        count1, count2 = 0, 0
        while cur1:
            sum1 += cur1.val * 10 ** count1
            count1 += 1
            cur1 = cur1.next
        while cur2:
            sum2 += cur2.val * 10 ** count2
            count2 += 1
            cur2 = cur2.next
        res = str(sum1 + sum2)
        head = tmp = ListNode(0)
        for i in range(len(res) - 1, -1, -1):
            cur = ListNode(int(res[i]))
            tmp.next = cur
            tmp = cur
        return head.next


class Solution:
    def addTwoNumbers(self, l1, l2):
        head = ListNode(0) #head是一个哑节点(dummy node)，可以简化代码, l和head指向的是可变对象，因而l变化了，head也会随之变化
        l = head
        carry = 0
        while l1 or l2 or carry:
            sum, carry = carry, 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            if sum > 9:
                carry = 1
                sum -= 10
            l.next = ListNode(sum)
            l = l.next
        return head.next
