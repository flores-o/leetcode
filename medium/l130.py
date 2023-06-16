"""
130. Surrounded Regions

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.
"""
from typing import List

class Solution:
    def markIsland(self, board: List[List[str]], r:int, c:int, markerChr: str) -> None:
        board[r][c] = markerChr
        if r > 0 and board[r-1][c] == 'O':
            self.markIsland(board, r-1, c, markerChr)
        if r < len(board)-1 and board[r+1][c] == 'O':
            self.markIsland(board, r+1, c, markerChr)
        if c > 0 and board[r][c-1] == 'O':
            self.markIsland(board, r, c-1, markerChr)
        if c < len(board[r])-1 and board[r][c+1] == 'O':
            self.markIsland(board, r, c+1, markerChr)

    def markBorder(self, board: List[List[str]]) -> None:
        for r in range(len(board)):
            if board[r][0] == 'O':
                self.markIsland(board, r, 0, 'B')
            if board[r][len(board[r])-1] == 'O':
                self.markIsland(board, r, len(board[r])-1, 'B')
        for c in range(len(board[0])):
            if board[0][c] == 'O':
                self.markIsland(board, 0, c, 'B')
            if board[len(board)-1][c] == 'O':
                self.markIsland(board, len(board)-1, c, 'B')

    def flipBorder(self, board: List[List[str]]) -> None:
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == 'B':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.markBorder(board)
        self.flipBorder(board)

if __name__ == '__main__':
    s = Solution()
    board = [["X","X","X","X"],
            ["X","O","O","X"],
            ["X","X","O","X"],
            ["X","O","X","X"]]
    s.solve(board)
    assert
