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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res, queue = [], deque()
        queue.append(root)
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(tmp)
        return res
    
if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    a = TreeNode(20)
    a.left = TreeNode(15)
    a.right = TreeNode(7)
    root.right = a
    S = Solution()
    print(S.levelOrder(root))
