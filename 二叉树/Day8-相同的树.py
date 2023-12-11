# coding:utf-8

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.val)
    
class Solution:
    def isSameTree(self, p:TreeNode, q:TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
if __name__ == '__main__':
    root_p = TreeNode(1)
    root_p.left = TreeNode(2)
    root_p.right = TreeNode(3)
    root_q = TreeNode(1)
    root_q.left = TreeNode(2)
    root_q.right = TreeNode(3)
    S = Solution()
    print(S.isSameTree(root_p, root_q))