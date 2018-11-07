"""
Binary Search Tree Iterator

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.

"""

#inorder traversal
#https://www.youtube.com/watch?v=HuaOkZitdkY

# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.pushLeft(root)


    def hasNext(self):
        """
        :rtype: bool
        """
        if self.stack != []：  #注意：这里self.stack != []而不是self.stack != None, 容易弄混
            return True
        else:
            return False


    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        self.pushLeft(node.right)
        return node.val

    def pushLeft(self, root):
        while root:
            self.stack.append(root)    #注意：是把root放到stack里面
            root = root.left


# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
