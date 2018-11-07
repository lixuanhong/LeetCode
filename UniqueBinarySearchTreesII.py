"""
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

#思路：接上一题，这题要求返回的是所有符合条件的二叉查找树，而上一题要求的是符合条件的二叉查找树的棵数，我们上一题提过，求个数一般思路是动态规划，
#而枚举的话，我们就考虑dfs了。dfs(start, end)函数返回以start，start+1，...，end为根的二叉查找树。


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        def dfs(start, end):
            if start > end:
                return [None]                    #返回结果是list
            res = []
            for rootval in range(start, end+1):  #rootval为根节点的值，从start遍历到end
                LeftTree = dfs(start, rootval-1)
                RightTree = dfs(rootval+1, end)
                for i in LeftTree:               #i遍历符合条件的左子树
                    for j in RightTree:          #j遍历符合条件的右子树
                        root = TreeNode(rootval)
                        root.left = i
                        root.right = j
                        res.append(root)
            return res

        if n == 0: return []           #如果不加这个边界条件，n = 0时返回[[]]
        return dfs(1, n)
