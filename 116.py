"""
Populating Next Right Pointers in Each Node

Given a binary tree

struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
Recursive approach is fine, implicit stack space does not count as extra space for this problem.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
Example:

Given the following perfect binary tree,

     1
   /  \
  2    3
 / \  / \
4  5  6  7
After calling your function, the tree should look like:

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \  / \
4->5->6->7 -> NULL

递归求解：
1.如果该节点有左子树：1）该节点有右子树 2）该节点没有右子树 递归该节点的左子树
2.如果该节点有右子树：1）该节点的next节点有左子树 2）该节点的next节点没有左子树
https://www.youtube.com/watch?v=3MFL7L8HnUc

"""

#class TreeLinkNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
#        self.next = None

class Solution:
    def connect(self, root):
        if root == None: return
        if (root.left != None):
            root.left.next = root.right
        if root.next != None and root.right != None:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
