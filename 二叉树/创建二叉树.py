# -*- coding: utf-8 -*-
# Author   : ZhangQing
# Time     : 2023/11/14 16:03
# File     : 创建二叉树.py
# Project  : Test
# Desc     :

class TreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

# B = TreeNode("B")
# C = TreeNode("C")
# A = TreeNode("A", B, C)
# A.left = B
# A.right = C
# root = A

A,B,C,D,E,F,G,H,I = [TreeNode(x) for x in "ABCDEFGHI"]
A.left = B
A.right = C
B.right = D
C.left = E
C.right = F
E.left = G
F.left = H
F.right = I

print(C.right)
