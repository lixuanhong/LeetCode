"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#递归
class Solution(object):
    def zigzagLevelOrder(self, root):
        def dfs(root, level, res):
            if root:
                if len(res) < level+1:
                    res.append([])
                if level % 2 == 1:
                    res[level].append(root.val)
                elif level % 2 == 0:
                    res[level].insert(0,root.val) #一定要注意，insert take 2 argument, 第一位是0表示从头插入！！！
                dfs(root.right, level+1, res)
                dfs(root.left, level+1, res)
            return res

        res = []
        return dfs(root, 0, res)

#非递归
class Solution(object):
    def zigzagLevelOrder(self, root):
        res = []
        if not root: return res
        level = [root]
        count = 0
        while level:
            next = []
            res.append([node.val for node in level])
            if count % 2 == 0: level = level[::-1] #因为后面顺序已经颠倒，需要始终保持从右到左，所以要倒回来！！
            for node in level:
                if node.right:
                    next.append(node.right)
                if node.left:
                    next.append(node.left)
            if count % 2 == 0:
                level = next
            elif count % 2 == 1:
                level = next[::-1]       #注意[::-1]和sorted的区别，前者是顺序颠倒（从后到前），后者是顺序（从小到大）/倒序（从大到小）
            count += 1
        return res

"""
list.sort(key=..., reverse=...)
sorted(list, key=..., reverse=...)
Note: Simplest difference between sort() and sorted() is: sort() doesn't return any value while, sorted() returns an iterable list.
"""
