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
    def generateTrees(self, n: int)-> List[TreeNode]:
        def generateTrees(start, end):
            if start > end:
                return [None, ]
            
            allTrees = []
            for i in range(start, end+1):
                #  获取所有可行的左子树集合
                leftTrees = generateTrees(start, i-1)

                # 获取所有可行的柚子树集合
                rightTrees = generateTrees(i+1, end)

                # 从左子树集合中选出一棵左子树，从柚子树集合中选出一棵右子树，拼接到根节点上
                for l in leftTrees:
                    for r in rightTrees:
                        currTree = TreeNode(i)
                        currTree.left = l
                        currTree.right = r
                        allTrees.append(currTree)

            return allTrees
        return generateTrees(1, n) if n else []
    
if __name__ == '__main__':
    S = Solution()
    print(S.generateTrees(3))
