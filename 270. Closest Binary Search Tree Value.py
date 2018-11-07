"""
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4
"""

"""
思路：
If target value K is present in given BST, then it's the node having minimum absolute difference.
If target value K is less than the value of current node then move to the left child.
If target value K is greater than the value of current node then move to the right child.
Time complexity : O(h) where h is height of given Binary Search Tree.
"""

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        min = float("inf")
        res = float("inf")
        while root:
            if abs(root.val - target) < min:
                min = abs(root.val - target)           #注意：这里一定是abs(root.val - target)
                res = root.val

            if target ==  root.val:
                break
            elif target < root.val:
                root = root.left
            else:
                root = root.right

        return res
