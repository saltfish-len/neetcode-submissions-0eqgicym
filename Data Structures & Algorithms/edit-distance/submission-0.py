class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # use dp
        # dp[i][j]: dist of word1[:i-1] word2[:j-1]
        # dp[i+1][j+1] = 1. same, dp[i][j]
        #                2. different, min(dp[i][j+1],dp[i+1][j],dp[i][j]) + 1

        m,n = len(word1),len(word2)
        dp = [[max(m,n) for _ in range(n+1)] for _ in range(m+1)]

        for i in range(m+1):
            # word1[:i-1] word2[0]
            dp[i][0] = i
        for j in range(n+1):
            # word1[:0] word2[:j-1]
            dp[0][j] = j
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                # same
                if word1[i-1]==word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                    continue
                else:
                    # different
                    dp[i][j] = min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1]) + 1
                    continue
        return dp[-1][-1]