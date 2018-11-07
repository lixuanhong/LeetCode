"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#递归 - 简单，就是O(1) space
class Solution:
    def isSameTree(self, p, q):
        if not p and not q: return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False

#My Solution - Accepted but use extra space 思路是把两颗数打印出来了
class Solution:
    def isSameTree(self, p, q):
        return self.preOrder(p, []) == self.preOrder(q, [])

    def preOrder(self, root, res):
        if root:
            res.append(root.val)
            if not root.left and root.right:
                res.append(None)
                self.preOrder(root.right, res)
            self.preOrder(root.left, res)
            self.preOrder(root.right, res)
        return res        

#非递归
class Solution:
    def isSameTree(self, p, q):
        if not p and not q: return True
        stackp, stackq = [p], [q]
        while len(stackp) > 0 and len(stackq) > 0:
            m = stackp.pop()
            n = stackq.pop()
            if not m and not n:
                continue
            elif not m or not n:
                return False
            elif m and n:
                if m.val != n.val:
                    return False
            stackp.append(m.left)
            stackp.append(m.right)
            stackq.append(n.left)
            stackq.append(n.right)
        return len(stackp) == 0 and len(stackq) == 0
