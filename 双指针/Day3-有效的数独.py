# coding:utf-8

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row = [[0] * 9 for _ in range(9)]
        col = [[0] * 9 for _ in range(9)]
        block = [[0] * 9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j]) - 1
                    b = (i // 3) * 3 + j // 3
                    if row[i][num] or col[j][num] or block[b][num]:
                        return False
                    row[i][num] = col[j][num] = block[b][num] = 1
        return True

if __name__ == '__main__':
    board = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    S = Solution()
    print(S.isValidSudoku(board))