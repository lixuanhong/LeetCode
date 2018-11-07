"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,15,7,20] root->left->right
inorder = [15,9,7,3,20]  left->root->right
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
    def buildTree(self, preorder, inorder):
        def helper(prestart, instart, inend, preorder, inorder):
            if prestart > len(preorder) - 1 or instart > inend:
                return None
            root = TreeNode(preorder[prestart])
            for i in range(instart, inend+1):
                if inorder[i] == root.val:
                    pos = i
            root.left = helper(prestart+1,instart, pos-1, preorder, inorder)
            root.right = helper(prestart+(pos-instart+1), pos+1, inend, preorder, inorder)
            return root

        if not preorder or not inorder or len(preorder) == 0 or len(preorder) != len(inorder):
            return None
        return helper(0, 0, len(inorder)-1, preorder, inorder)
