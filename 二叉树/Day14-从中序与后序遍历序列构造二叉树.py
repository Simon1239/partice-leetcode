# coding:utf-8

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.val)
    
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(in_left, in_right):
            if in_left > in_right:
                return None
            
            val = postorder.pop()
            root = TreeNode(val)

            index= idx_map[val]

            root.right = helper(index+1, in_right)
            root.left = helper(in_left, index-1)
            return root

        idx_map = {val:idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder)-1)
    
if __name__ == '__main__':
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    S = Solution()
    print(S.buildTree(inorder, postorder))
