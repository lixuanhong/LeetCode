"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#BFS
class Solution:
    def levelOrderBottom(self, root):
        res = []
        if not root: return res
        curr = [root]
        level = 0
        while curr:
            next = []
            res.insert(0, [n.val for n in curr])
            for n in curr:
                if n.left:
                    next.append(n.left)
                if n.right:
                    next.append(n.right)
            curr = next
        return res

#DFS
class Solution:
    def levelOrderBottom(self, root):
        def helper(root, level, res):
            if root:
                if len(res) < level + 1:
                    res.append([])
                res[level].append(root.val)
                helper(root.left, level + 1, res)
                helper(root.right, level + 1, res)
            return res

        ans = []
        ans = helper(root, 0, [])
        ans.reverse() #This method does not return any value but reverse the given object from the list
        return ans
