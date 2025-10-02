class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        if not board:
            return
        
        for i in range(len(board[0])):
            if board[0][i] == 'O':
                self.dfs(board, 0, i)
            if board[len(board) - 1][i] == 'O':
                self.dfs(board, len(board) - 1, i)

        for i in range(len(board)):
            if board[i][0] == 'O':
                self.dfs(board, i, 0)
            if board[i][len(board[0]) - 1] == 'O':
                self.dfs(board, i, len(board[0]) - 1)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'Y':
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"




    def dfs(self, board, i, j):
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != 'O':
            return

        board[i][j] = 'Y'

        self.dfs(board, i+1, j)
        self.dfs(board, i-1, j)
        self.dfs(board, i, j+1)
        self.dfs(board, i, j-1)