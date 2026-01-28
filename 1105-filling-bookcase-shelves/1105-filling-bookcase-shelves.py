class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        
        dp = [float('inf')] * (len(books) + 1)
        dp[0] = 0
        
        for i in range(1, len(books) + 1):

            w = 0
            h = 0

            for j in range(i, 0, -1):

                w += books[j-1][0]

                if w > shelfWidth:
                    break
    
                h = max(h, books[j-1][1])

                dp[i] = min(dp[i], dp[j-1] + h)
        
        return dp[len(books)]