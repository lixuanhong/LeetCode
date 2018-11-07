"""
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples 1:

Input: [3,9,20,null,null,15,7]

   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7

Output:

[
  [9],
  [3,15],
  [20],
  [7]
]
Examples 2:

Input: [3,9,8,4,0,1,7]

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7

Output:

[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]
Examples 3:

Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2

Output:

[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        resultMap = {}
        queue = [(root, 0)]
        while len(queue) > 0:
            node, col = queue.pop(0)
            if node is None:
                continue
            resultMap[col] = resultMap.get(col, []) + [node.val] # get()第二个参数是default, 如果key不存在，返回default值！
            queue.append((node.left, col - 1))
            queue.append((node.right, col + 1))
        result = []
        i = 0
        while i in resultMap:
            result.insert(0, resultMap.get(i))
            i -= 1
        i = 1
        while i in resultMap:
            result.append(resultMap.get(i))
            i += 1
        return result
