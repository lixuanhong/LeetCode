"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

"""

class RandomListNode(object):
    def__init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        listMap = {}
        cur = head
        while (cur != None):
            listMap[cur] = RandomListNode(cur.label)
            cur = cur.next
        cur = head
        while (cur != None):
            listMap.get(cur).next = listMap.get(cur.next)
            listMap.get(cur).random = listMap.get(cur.random)
            cur = cur.next
        return listMap.get(head)
