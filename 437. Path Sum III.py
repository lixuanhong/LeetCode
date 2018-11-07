"""
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""

"""
思路：2DFS
1st： recursively travel tree to find answers of current node + ans of left child + ans of right child.
2nd: find the path from current node to child that adds up to sum
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.res = 0

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root is None:
            return
        self.helper(root, sum)
        self.pathSum(root.left, sum)
        self.pathSum(root.right, sum)
        return self.res

    def helper(self, root, sum):
        if root is None:
            return
        if root.val == sum:
            self.res += 1
        self.helper(root.left, sum - root.val)
        self.helper(root.right, sum - root.val)
