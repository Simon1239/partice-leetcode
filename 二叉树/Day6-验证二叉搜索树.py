# coding:utf-8

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.val)
    
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower=float('-inf'), upper=float('inf')) -> bool:
            if not node:
                return True
            
            val = node.val
            if val <= lower or val >= upper:
                return False
            
            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True
        
        return helper(root)
    
if __name__=='__main__':
    root=TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    S = Solution()
    print(S.isValidBST(root))