class Node(object):
    def __init__(self, x, left, right):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def treeToDoublyList(self, root):
        if not root:
            return None
        head, tail = self.helper(root)
        return head

    def helper(self, root):
        head, tail = root, root
        if root.left:
            lhead, ltail = self.helper(root.left)
            ltail.right = root
            root.left = ltail
            head = lhead
        if root.right:
            rhead, rtail = self.helper(root.right)
            rhead.left = root
            root.right = rhead
            tail = rtail
        head.left = tail
        tail.right = head
        return (head, tail)
