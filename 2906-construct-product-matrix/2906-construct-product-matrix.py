class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        
        MOD = 12345
        n, m = len(grid), len(grid[0])
        
        arr = []
        for i in range(n):
            for j in range(m):
                arr.append(grid[i][j] % MOD)

        size = len(arr)

        prefix = [1] * size
        suffix = [1] * size

        for i in range(1, size):
            prefix[i] = (prefix[i - 1] * arr[i - 1]) % MOD

        for i in range(size - 2, -1, -1):
            suffix[i] = (suffix[i + 1] * arr[i + 1]) % MOD

        result = [[0] * m for _ in range(n)]

        for i in range(size):
            r = i // m
            c = i % m
            result[r][c] = (prefix[i] * suffix[i]) % MOD

        return result

        