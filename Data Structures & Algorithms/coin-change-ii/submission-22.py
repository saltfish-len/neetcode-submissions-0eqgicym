class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        # dp[i][j] = change with amount = i and coins[:j]
        # dp[i][j] = use current coin dp[i-c][j]
        #            skip dp[i][j-1]

        n = len(coins)
        dp = [[0]*(n+1) for _ in range(amount+1)]
        
        for j in range(n+1):
            dp[0][j] = 1

        for i in range(1,amount+1):
            for j in range(1,n+1):
                c = coins[j-1]
                if c > i:
                    dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-c][j]
            
        return dp[amount][n]
                    