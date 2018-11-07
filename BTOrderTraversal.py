"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#DFS 递归方法
class Solution:
    def levelOrder(self, root):
        def helper(root, level, res):
            if root:
                if len(res) < level+1:
                    res.append([])
                res[level].append(root.val)
                helper(root.left, level + 1, res) #从最左边那个分支往下扫描，然后右边的依次往里添加
                helper(root.right, level + 1, res)
            return res

        return helper(root, 0, [])

#BFS 非递归方法
class Solution:
    def levelOrder(self, root):
        res = []
        if not root: return res
        level = [root]                         #一层一层地扫描
        while level:
            next = []
            res.append([n.val for n in level])
            for node in level:
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            level = next
        return res
