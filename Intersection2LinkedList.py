"""
Write a program to find the node at which the intersection of two singly linked lists begins.
For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if headA == None or headB == None:
            return None
        p, q = headA, headB
        while p != None and q != None and p != q: #如果p == q, 直接return p
            p = p.next
            q = q.next
            if p == q:
                return p       #如果p, q都是None, 直接return None
            if p == None:
                p = headB
            if q == None:
                q = headA
        return p             #这里是如果p == q不进入while循环，那么return p 

# My Solution - 思路一样，没有这么优化，可被AC
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        l1, l2, l = 0, 0, 0
        tmp1, tmp2 = headA, headB
        while tmp1:
            l1 += 1
            tmp1 = tmp1.next
        while tmp2:
            l2 += 1
            tmp2 = tmp2.next
        l = l1 + l2
        i = 0
        h1, h2 = headA, headB
        while i < l:
            if h1 == h2:
                return h1
            else:
                h1 = h1.next
                h2 = h2.next
                i += 1
                if not h1:
                    h1 = headB
                if not h2:
                    h2 = headA
        return None

#思路：双指针解法 (O(n+m) 时间, O(1) 空间)

#维护两个指针pA和pB，初始分别指向A和B。然后让它们分别遍历整个链表，每步一个节点。

#当pA到达链表末尾时，让它指向B的头节点（没错，是B）；类似的当pB到达链表末尾时，重新指向A的头节点。

#如果pA在某一点与pB相遇，则pA/pB就是交点。

#考虑两个链表：A = {1,3,5,7,9,11} B = {2,4,9,11}，它们的交点是节点'9'。由于B的长度是4 小于 A的长度6，pB会首先到达链表的末尾，由于pB比pA恰好少走2个节点。通过把pB指向A的头，把pA指向B的头，我们现在让pB比pA恰好多走2个节点。所以在第二轮，它们可以保证同时在交点相遇。

#如果两个链表有交点，则它们的最后一个节点一定是同一个节点。所以当pA/pB到达链表末尾时，分别记录下A和B的最后一个节点。如果两个链表的末尾节点不一致，说明两个链表没有交点。”“”
