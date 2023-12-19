# coding:utf-8

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.val)

class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1
        
if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    a = TreeNode(20)
    a.left = TreeNode(15)
    a.right = TreeNode(7)
    root.right = a
    S = Solution()
    print(S.maxDepth(root))