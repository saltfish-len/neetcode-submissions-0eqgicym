class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[i][j]: number of unique path for ixj
        # dp[i][j]: last=down dp[i-1][j]+
        #           last=right dp[i][j-1]


        dp = [[0]*n for _ in range(m)] 
        if m==1 or n==1:
            return 1
        
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]