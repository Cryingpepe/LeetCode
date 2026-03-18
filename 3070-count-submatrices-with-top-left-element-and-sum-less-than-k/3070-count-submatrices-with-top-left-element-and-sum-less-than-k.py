class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        
        result = 0

        for i in range(1, len(grid[0])):
            grid[0][i] += grid[0][i - 1]

        for i in range(1, len(grid)):
            grid[i][0] += grid[i - 1][0]

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][j] += (grid[i - 1][j] + grid[i][j - 1] - grid[i - 1][j - 1])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] <= k:
                    result += 1

        return result
