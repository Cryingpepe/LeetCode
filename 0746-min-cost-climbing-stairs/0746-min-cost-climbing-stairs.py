class Solution(object):
    def minCostClimbingStairs(self, cost):
        
        n = len(cost)

        dp = [0 for i in range(n)]

        dp[0] = cost[0] # initial values
        dp[1] = cost[1] # initial values

        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2]) # the minimum cost for i-th stair


        return min(dp[n-1], dp[n-2]) # to get top, need to move 2 steps from n-2 or 1 stpe from n-1