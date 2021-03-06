"""
Given a node from a cyclic linked list which is sorted in ascending order, write a function to insert a value into the list such that it remains a cyclic sorted list. The given node can be a reference to any single node in the list, and may not be necessarily the smallest value in the cyclic list.

If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the insertion, the cyclic list should remain sorted.

If the list is empty (i.e., given node is null), you should create a new single cyclic list and return the reference to that single node. Otherwise, you should return the original given node.

The following example may help you understand the problem better:
In the figure above, there is a cyclic sorted list of three elements. You are given a reference to the node with value 3, and we need to insert 2 into the list.
The new node should insert between node 1 and node 3. After the insertion, the list should look like this, and we should still return node 3.
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""
class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        n = Node(insertVal, next)              #注意：这里是两个参数
        if head is None:                       #head，pre和cur都是Node!!
            n.next = n
            return n
        pre, cur = head, head.next
        while cur != head:                     #注意循环条件(非单个Node循环)！！
            if pre.val <= insertVal and cur.val >= insertVal:
                break
            if pre.val > cur.val and (pre.val < insertVal or cur.val > insertVal):
                break
            pre, cur = pre.next, cur.next
        pre.next = n                    # 即使单个Node循环也满足
        n.next = cur
        return head
