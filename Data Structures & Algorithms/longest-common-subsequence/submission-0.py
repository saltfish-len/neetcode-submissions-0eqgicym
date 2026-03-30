class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp[i][j]: LCS(text1[0...i],text2[0...j])
        # dp[i][j] = max t[i]==t[j] 1+dp[i-1][j-1] use i j
        #                t[i]!=t[j] dp[i-1][j], dp[i][j-1] dont use i j
        
        m,n = len(text1),len(text2)
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m+1):
            dp[i][0] = 0
        for j in range(n+1):
            dp[0][j] = 0

        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j] = max([int(text1[i-1] == text2[j-1]) + dp[i-1][j-1],
                                dp[i-1][j], dp[i][j-1]])
        
        return dp[m][n]