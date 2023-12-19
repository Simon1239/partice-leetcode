# coding:utf-8

from typing import Optional
from typing import List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.val)

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        res, _deque = [], deque([root])
        while _deque:
            tmp = deque()
            for _ in range(len(_deque)):
                node = _deque.popleft()
                if len(res) % 2 == 0: tmp.append(node.val) 
                else: tmp.appendleft(node.left)
                if node.left: _deque.append(node.left)
                if node.right: _deque.append(node.right)
            res.append(list(tmp))
        return res
    
if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    a = TreeNode(20)
    a.left = TreeNode(15)
    a.right = TreeNode(7)
    root.right = a
    S = Solution()
    print(S.zigzagLevelOrder(root))