"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        def helper(poststart, instart, inend, inorder, postorder):
            if poststart < 0 or instart > inend:
                return None
            root = TreeNode(postorder[poststart])
            idx = 0
            for i in range(instart, inend+1):
                if inorder[i] == root.val:
                    idx = i
            root.right = helper(poststart-1, idx+1, inend, inorder, postorder)
            root.left = helper(poststart-(inend-idx+1), instart, idx-1, inorder, postorder)
            return root

        if not inorder or not postorder or len(inorder) == 0 or len(inorder) != len(postorder):
            return None
        return helper(len(postorder)-1, 0, len(inorder)-1, inorder, postorder)
