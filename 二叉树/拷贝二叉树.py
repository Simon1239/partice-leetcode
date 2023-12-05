# -*- coding: utf-8 -*-
# Author   : ZhangQing
# Time     : 2023/11/14 18:06
# File     : 拷贝二叉树.py
# Project  : Test
# Desc     :

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

def copyTree(node):
    if node is None:
        return None

    lt = copyTree(node.left)
    lr = copyTree(node.right)

    return TreeNode(node.data, lt, lr)

if __name__ == '__main__':
    root = createTree()
    newTree = copyTree(root)
    print(levelOrder(newTree))