"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:

Input:
    2
   / \
  1   3
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.
"""

"""
思路：检查每一个node是否在区间之内，最开始区间在float("-inf") - float("inf")之间，遍历过程中不断更新这个区间的范围
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        def isValidBST(self, root):
            min, max = float("-inf"), float("inf")
            return self.isBST(root, min, max)

        def isBST(self, root, min, max):
            if not root:
                return True
            if root.val <= min or root.val >= max:
                return False
            return self.isBST(root.left, min, root.val) and self.isBST(root.right, root.val, max)
