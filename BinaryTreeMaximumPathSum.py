"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum(self, root):
         """
        :type root: TreeNode
        :rtype: int
        """

        def helper(root):                            #这个helper函数是计算经过root根节点的最大path, 必须满足两个条件：1. path经过root 2. 最多只能使用一个child, 不可能两个都使用！
            if not root:
                return float("-inf")
            l = max(0, helper(root.left))
            r = max(0, helper(root.right))
            self.res = max(self.res, l+r+root.val)    #求结果的时候，针对所有节点左边的最大值加上右边的最大值加上本身，来更新最大path sum, 所以可以两边都使用！！
            return max(l, r) + root.val               #该函数不可能同时使用两个子节点然后再返回根节点，因此只能选择最大的一个子节点返回根节点

        self.res = float("-inf")                     #定义全局变量
        helper(root)
        return self.res
