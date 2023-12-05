# -*- coding: utf-8 -*-
# Author   : ZhangQing
# Time     : 2023/11/14 17:05
# File     : 二叉树的深度.py
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

def depth(node):
    if node is None:
        return 0

    dl = depth(node.left)
    dr = depth(node.right)

    return max(dl, dr) + 1

from collections import deque
def depth2(root):
    q = deque([(root, 1)])
    while q:
        node, d = q.popleft()
        if node.left:
            q.append((node.left, d+1))
        if node.right:
            q.append((node.right, d+1))

    return d

if __name__ == '__main__':
    root = createTree()
    print(depth(root))
    print(depth2(root))