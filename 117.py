"""
Populating Next Right Pointers in Each Node II

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
Example:

Given the following binary tree,

     1
   /  \
  2    3
 / \    \
4   5    7
After calling your function, the tree should look like:

                 1 -> NULL
               /  \
root          2 -> 3 -> NULL
             / \    \
            4-> 5 -> 7 -> NULL
    childHead
              child

使用层次遍历：

临时节点指向根节点的左子树，如果左子树存在，临时节点下移；如果不存在，临时节点指向根节点的右子树；如果右子树存在，临时节点下移
根节点下移，如果根节点不为空，重复步骤1，否则，重置临时节点，将根节点移至下一层的首节点
https://www.cnblogs.com/slurm/p/5318764.html 需要巩固！！

"""

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        node = tmp = TreeLinkNode(0)

        while root:
            node.next = root.left
            if node.next:
                node = node.next
            node.next = root.right
            if node.next:
                node = node.next
            root = root.next
            if not root:
                node = tmp
                root = node.next
