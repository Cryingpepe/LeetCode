class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s) == 1:
            return s

        maxLength = 1
        result = s[0]
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = True

            for j in range(i):
                if s[j] == s[i] and (i - j < 3 or dp[j + 1][i - 1]):
                    dp[j][i] = True

                    if i - j + 1 > maxLength:
                        maxLength = i - j + 1
                        result = s[j:i + 1]

        return result
