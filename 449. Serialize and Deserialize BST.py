"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
"""

"""
思路：这个题采用前序遍历的方式，这样，遍历得到的第一个数组就是BST的根节点，数组后面的这些数中比根节点的值小的是根节点的左子树，比根节点值大的是根节点的右子树（BST的最重要性质）。

因此，重要结论：BST的前序遍历能唯一的确定一颗BST！！
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def __init__(self):
        self.vals = []

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        self.preOrder(root)
        return " ".join(map(str, self.vals))    #注意：用空格链接来区分不同数字，join里面必须是string sequence


    def preOrder(self, root):
        if root:
            self.vals.append(root.val)
            self.preOrder(root.left)
            self.preOrder(root.right)



    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        self.vals = collections.deque(int(val) for val in data.split())  #注意：split()的默认分隔符就是空格！！
        return self.build(float("-inf"), float("inf"))

    def build(self, minVal, maxVal):
        if self.vals and minVal < self.vals[0] < maxVal:
            val = self.vals.popleft()
            root = TreeNode(val)
            root.left = self.build(minVal, val)
            root.right = self.build(val, maxVal)
            return root
