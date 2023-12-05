# -*- coding: utf-8 -*-
# Author   : ZhangQing
# Time     : 2023/11/15 16:29
# File     : 二叉搜索树.py
# Project  : Test
# Desc     :

class TreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

from collections import deque

def levelOrder(root):
    q = deque([root])
    while q:
        node = q.popleft()
        print("{}({},{})".format(node, node.left, node.right))

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    # def search(self, k):
    #     node = self.root
    #     while node and node.data != k:
    #         if k < node.data:
    #             node = node.left
    #         else:
    #             node = node.right
    #     return node

    def search(self, k):
        node, _ = self._search(k)
        return node

    def _search(self, k):
        parent = None
        node = self.root
        while node and node.data != k:
            parent = node
            if k < node.data:
                node = node.left
            else:
                node = node.right
        return node, parent


    def insert(self, k):
        node, parent = self._search(k)
        if node:
            return

        node = TreeNode(k)
        if parent is None: # 空树
            self.root = node
        elif k < parent.data:
            parent.left = node
        else:
            parent.right = node

    def delete(self, k):
        pass

if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    # levelOrder(bst.root)
    bst.insert(1)
    bst.insert(2)
    bst.insert(12)
    bst.insert(8)
    levelOrder(bst.root)
    # print(bst.search(12))
    # print(bst.search(17))