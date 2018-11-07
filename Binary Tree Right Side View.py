"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root is None: return res
        self.helper(root, res, 0)
        return res

    def helper(self, root, res, level):
        if root is None: return
        if len(res) == level:
            res.append(root.val)
        self.helper(root.right, res, level+1)
        self.helper(root.left, res, level+1)
