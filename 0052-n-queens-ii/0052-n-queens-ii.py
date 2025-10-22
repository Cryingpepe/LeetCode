class Solution:
    def totalNQueens(self, n: int) -> int:
        
        self.result = 0 
        col, pos, neg = set(), set(), set()
        
        def backtrack(r):

            if n == r:
                self.result += 1

            for c in range(n):
                if c in col or (c + r) in pos or (r - c) in neg:
                    continue

                col.add(c)
                pos.add(c + r)
                neg.add(r - c)

                backtrack(r + 1)

                col.remove(c)
                pos.remove(c + r)
                neg.remove(r - c)
                
        backtrack(0)

        return self.result