class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        n, m = len(obstacleGrid[0]), len(obstacleGrid)
        dp = [[0] * n for _ in range(m)]

        for i in range(n):
            if obstacleGrid[0][i] == 1:
                break
            else:
                dp[0][i] = 1

        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            else:
                dp[i][0] = 1

        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[j][i]:
                    dp[j][i] = 0
                else:
                    dp[j][i] = dp[j - 1][i] + dp[j][i - 1]
        
        return dp[m - 1][n - 1]