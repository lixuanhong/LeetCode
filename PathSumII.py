"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root, sum):
        def helper(root, sum, path, res):
            if not root: return
            if not root.left and not root.right:
                if root.val == sum:
                    res.append(path)
                    return
            if root.left:
                helper(root.left, sum - root.val, path+[root.left.val], res)
            if root.right:
                helper(root.right, sum - root.val, path+[root.right.val], res)


        if not root: return []
        res = []
        path = [root.val] #我之前的错误在于把path设置成为[], 然后用path.append(root.val),在递归的时候不同路径造成path的混乱，把所有路径都添加到了path里面去
        helper(root, sum, path, res)
        return res
