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
    def buildTree(self, preorder: List[int], inorder:[int]) -> TreeNode:
        def myBuildTree(preorder_left: int, preorder_right: int, inorder_left: int, inorder_right: int):
            if preorder_left > preorder_right:
                return None
            
            # 前序遍历中的第一个结点就是根节点
            preorder_root = preorder_left
            #  在中序遍历中定位根节点
            inorder_root = index[preorder[preorder_root]]