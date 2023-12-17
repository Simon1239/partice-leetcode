# coding:utf-8

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.val)
    
class Solution:
    def isSymmetric(self, root:Optional[TreeNode]) -> bool:
        def recur(L, R):
            if not L and not R: return True
            if not L or not R or L.val != R.val: return False
            return recur(L.left, R.right) and recur(L.right, R.left)
        
        return not root or recur(root.left, root.right)
    
if __name__ == '__main__':
    root = TreeNode(1)
    a = TreeNode(2)
    a.left = TreeNode(3)
    a.right = TreeNode(4)
    root.left = a
    b = TreeNode(2)
    b.left = TreeNode(4)
    b.right = TreeNode(3)
    root.right = b
    S = Solution()
    print(S.isSymmetric(root))
