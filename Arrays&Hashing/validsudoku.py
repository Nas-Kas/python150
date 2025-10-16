from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for x in range(0, 9):
            if self.isValidRow(board,x) == False:
                return False
            if self.isValidCol(board,x) == False:
                return False
        
        for x in range(0,9,+3):
            for y in range(0,9,+3):
                if self.isValidSquare(board,x,y) == False:
                    return False
        
        return True

    def isValidSquare(self, board, row, col):
        dokuSet = set()
        rowend = row + 3
        colend = col + 3
        for r in range(row, row + 3): # careful about name reuse for row in range will throw things off
            for c in range(col, col + 3):
                if board[r][c] in dokuSet:
                    return False
                elif board[r][c] != '.':
                    dokuSet.add(board[r][c])
        return True
    
    def isValidRow(self, board, row):
        dokuSet = set()
        for x in range(0,len(board[row])):
            if board[row][x] in dokuSet:
                return False
            elif board[row][x] != '.':
                dokuSet.add(board[row][x])
        return True

    def isValidCol(self, board, col):
        dokuSet = set()
        for x in range(0, len(board)):
            if board[x][col] in dokuSet:
                return False
            elif board[x][col] != '.':
                dokuSet.add(board[x][col])
        return True
    
    
board = [
 ["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]
]

board2=[
[".",".",".","9",".",".",".",".","."],
[".",".",".",".",".",".",".",".","."],
[".",".","3",".",".",".",".",".","1"],
[".",".",".",".",".",".",".",".","."],
["1",".",".",".",".",".","3",".","."],
[".",".",".",".","2",".","6",".","."],
[".","9",".",".",".",".",".","7","."],
[".",".",".",".",".",".",".",".","."],
["8",".",".","8",".",".",".",".","."]
]




s = Solution()
print(s.isValidSudoku(board2))
