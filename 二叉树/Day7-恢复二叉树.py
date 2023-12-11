# coding:utf-8

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.val)
    
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        firstNode = None
        secondNode = None
        pre = TreeNode(float('-inf'))

        stack = []
        p = root
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()

            if not firstNode and pre.val > p.val:
                firstNode = pre
            if firstNode and pre.val > p.val:
                secondNode = p
            pre = p
            p = p.right

        firstNode.val, secondNode.val = secondNode.val, firstNode.val

class Solution:
    def recoverTree(self, root:TreeNode) -> None:
        self.firstNode = None
        self.secondNode = None
        self.preNode = TreeNode(float('-inf'))

        def in_order(root):
            if not root:
                return
            in_order(root.left)
            if self.firstNode == None and self.preNode.val >= root.val:
                self.firstNode = self.preNode
            if self.firstNode and self.preNode.val >= root.val:
                self.secondNode = root
            self.preNode = root
            in_order(root.right)

        in_order(root)
        self.firstNode.val, self.secondNode.val = self.secondNode.val, self.firstNode.val

if __name__ == '__main__':
    root = TreeNode(1)
    a = TreeNode(3)
    b = TreeNode(2)
    a.right = b
    root.left = a
    S = Solution()
    S.recoverTree(root)
    print(root)
