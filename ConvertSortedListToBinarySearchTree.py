"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""

#思路：一，可以使用快慢指针来找到中间的那个节点，然后将这个节点作为树根，并分别递归这个节点左右两边的链表产生左右子树，这样的好处是不需要使用额外的空间，坏处是代码不够整洁。
# 二，将排序好的链表的每个节点的值存入一个数组中二，将排序好的链表的每个节点的值存入一个数组中，代码比较简洁
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#用快慢指针找中间点
class Solution(object):
    def sortedListToBST(self, head):
        if not head: return None
        if not head.next: return TreeNode(head.val)
        def findmid(head):
            slow = fast = head
            pre = None
            while fast and fast.next:
                pre = slow
                slow = slow.next
                fast = fast.next.next
            pre.next = None
            return slow

        mid = findmid(head)
        root = TreeNode(mid.val)
        root.left = self.sortedListToBST(head) #从head到mid-1
        root.right = self.sortedListToBST(mid.next) #从mid+1到Tail
        return root

#思路：将linked list转化为list, 然后用递归
class Solution(object):
    def sortedArrayToBST(self, array):
        mid = len(array)/2
        if length == 0:
            return None
        if length == 1:
            return TreeNode(array[0])
        root = TreeNode(array[mid])
        root.left = sortedArrayToBST(array[:mid]) #Excluding mid point
        root.right = sortedArrayToBST(array[mid+1:]) #Excluding mid point
        return root


    def sortedListToBST(self, head):
        if head = None: return head
        array = []
        while head != None:
            array.append(head.val)
            head = head.next
        return self.sortedArrayToBST(array)
