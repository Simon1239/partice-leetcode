# -*- coding: utf-8 -*-
# Author   : ZhangQing
# Time     : 2023/11/14 16:30
# File     : 遍历二叉树.py
# Project  : Test
# Desc     : 先序遍历：先根节点，在左子树，在右子树；中序遍历：；后序遍历：；层序遍历：；

class TreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

def createTree():
    A, B, C, D, E, F, G, H, I = [TreeNode(x) for x in "ABCDEFGHI"]
    A.left = B
    A.right = C
    B.right = D
    C.left = E
    C.right = F
    E.left = G
    F.left = H
    F.right = I
    return A

def preOrder(node):
    if node is None:
        return

    print(node.data)
    preOrder(node.left)
    preOrder(node.right)

def inOrder(node):
    if node is None:
        return

    preOrder(node.left)
    print(node.data)
    preOrder(node.right)

def postOrder(node):
    if node is None:
        return

    preOrder(node.left)
    preOrder(node.right)
    print(node.data)

def preOrderIter(root):
    s = []
    node = root

    while True:
        while node:
            print(node)
            s.append(node)
            node = node.left

        # 回溯
        if not s:
            break
        node = s.pop().right

from collections import deque

def levelOrder(root):
    q = deque([root])
    while q:
        node = q.popleft()
        print(node)

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

if __name__ == '__main__':
    root = createTree()
    # preOrder(root)
    # inOrder(root)
    # postOrder(root)
    # preOrderIter(root)
    levelOrder(root)