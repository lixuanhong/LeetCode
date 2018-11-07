"""
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""

"""
https://www.youtube.com/watch?v=FypgA5sRrog
"""

#class TreeNode(object):
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
#

# My Solution - Accepted
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        res = []
        if not root:
            return []
        return self.dfs(root, res, "")

    def dfs(self, root, res, s):
        if not root:
            return
        if not root.left and not root.right:
            s += str(root.val)
            res.append(s)
        if root.left or root.right:
            s += str(root.val) + "->"
        self.dfs(root.left, res, s)
        self.dfs(root.right, res, s)
        return res


##################################################################################


class Solution(object):

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        res = []
        if not root: return res
        helper(root, res, "")
        return res

    def helper(self, root, res, path):
        if not root.left and not root.right:
            res.append(path + str(root.val))

        if root.left:
            self.helper(root.left, res, path + str(root.val) + "->")

        if root.right:
            self.helper(root.right, res, path + str(root.val) + "->")
