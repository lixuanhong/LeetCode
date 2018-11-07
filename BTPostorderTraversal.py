"""
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        def helper(root, res):
            if not root:
                return res
            helper(root.left, res)
            helper(root.right, res)
            res.append(root.val)
            return res

        res = []
        return helper(root, res)
