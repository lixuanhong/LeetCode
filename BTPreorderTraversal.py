"""
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        def helper(root, res):
            if not root:
                return res
            res.append(root.val)
            helper(root.left, res)
            helper(root.right, res)
            return res

        res = []
        return helper(root, res)
