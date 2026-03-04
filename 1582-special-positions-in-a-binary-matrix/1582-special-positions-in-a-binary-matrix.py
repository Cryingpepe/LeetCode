class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:

        row = collections.defaultdict(int)
        column = collections.defaultdict(int)
        result = 0

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]:
                    row[i] += 1
                    column[j] += 1

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] and row[i] == 1 and column[j] == 1:
                    result += 1

        return result
        
        
