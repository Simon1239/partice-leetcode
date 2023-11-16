# -*- coding: utf-8 -*-
# Author   : ZhangQing
# Time     : 2023/11/6 21:32
# File     : 二叉树剪枝.py
# Project  : practice-leet-code
# Desc     :
from typing import Optional


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self,root_value):
        self.root = TreeNode(root_value)

    def insert(self,value):
        self._insert_recursive(self.root,value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = TreeNode(value)
            else:
                self._insert_recursive(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = TreeNode(value)
            else:
                self._insert_recursive(current_node.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current_node, value):
        if current_node is None:
            return False
        if current_node.value == value:
            return True
        elif value < current_node.value:
            return self._search_recursive(current_node.left, value)
        else:
            return self._search_recursive(current_node.right, value)
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.left is None and root.right is None and root.val == 0:
            return None
        return root

if __name__ == '__main__':
    tree = TreeNode(1)
    print(tree)

