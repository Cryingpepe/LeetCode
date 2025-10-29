class Solution:

    def backtrack(self, x, y, num, board, word):
        
        if num == len(word):
            return True
        
        if x < 0 or x >= len(board[0]) or y < 0 or y >= len(board):
            return False
        
        if board[y][x] != word[num]:
            return False
        
        temp = board[y][x]
        board[y][x] = "#"
        
        res = self.backtrack(x+1, y, num+1, board, word) or self.backtrack(x-1, y, num+1, board, word) or self.backtrack(x, y+1, num+1, board, word) or self.backtrack(x, y-1, num+1, board, word)

        board[y][x] = temp
        
        return res


    def exist(self, board: List[List[str]], word: str) -> bool:
        
        if not board:
            return False
        
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == word[0]:
                    if self.backtrack(x, y, 0, board, word):
                        return True
        
        return False


        