"""
Given a binary tree rooted at root, the depth of each node is the shortest distance to the root.

A node is deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is that node, plus the set of all descendants of that node.

Return the node with the largest depth such that it contains all the deepest nodes in its subtree.

Example 1:

Input: [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation:

We return the node with value 2, colored in yellow in the diagram.
The nodes colored in blue are the deepest nodes of the tree.
The input "[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]" is a serialization of the given tree.
The output "[2, 7, 4]" is a serialization of the subtree rooted at the node with value 2.
Both the input and output have TreeNode type.
"""

"""
思路：自下而上，每个left node的depth为0；如果左右子树返回depth相等，那么subtree node就是root; 如果左子树返回depth大，返回(dl+1, sl); 否则返回(dr+1, sr)
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def depth(self, root):
            if not root:
                return (-1, None)                #返回（深度，节点）pair
            dl, sl = depth(root.left)            #返回depth of left subtree and node of left subtree
            dr, sr = depth(root.right)
            if dl == dr: return (dl+1, root)
            if dl > dr:
                return (dl+1, sl)
            else:
                return (dr+1, sr)

        if not root:
            return None
        return depth(root)[1]
