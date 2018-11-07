"""
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""

"""
思路：1. 将root排列好的右子数接到root左子树最右侧的node
     2. 将root排列好的左子树替换root的右子数
     3. 将root左子树设为None
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        if not root:
            return None

        self.flatten(root.left)                 #先排左子树
        self.flatten(root.right)                #再排列右子树

        if root.left == None:                   #如果左子树没有，说明已经完成排列，返回即可；这里用return None也可以
            return
        node = root.left                        #找到左子树的node
        while node.right != None:               #找到左子树最右侧的node,做为连接点
            node = node.right
        node.right = root.right                 #将右子树排列好的序列接到左子树连接node上面
        root.right = root.left                  #将排列好的左子树替换右子树
        root.left = None                        #将左子树设为None
