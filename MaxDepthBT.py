"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#DFS
class Solution:
    def maxDepth(self, root):
        def helper(root, level, res):
            node = [root]
            if root:
                if len(res) < level + 1:
                    res.append([])
                res[level].append(root.val)
                helper(root.left, level + 1, res)
                helper(root.right, level + 1, res)
            return len(res)
        return helper(root, 0, [])

#BFS
class Solution:
    def maxDepth(self, root):
        res = []
        if not root: return 0
        curr = [root]
        while curr:
            next = []
            res.append(n.val for n in curr)
            for n in curr:
                if n.left:
                    next.append(n.left)
                if n.right:
                    next.append(n.right)
            curr = next
        return len(res)

#递归
class Solution:
    def maxDepth(self, root):
        if root == None:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
