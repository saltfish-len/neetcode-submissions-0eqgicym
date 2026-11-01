class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # min(1+coinChange(coins, amount - c) for c in coins)
        # dp[i] = coinChange(coins, i)
        dp = {0:0}

        def change(t):
            if t in dp:
                return dp[t]
 
            res = 1e9
            for c in coins:
                if t - c >= 0:
                    res = min(1 + change(t-c),res)

            dp[t] = res
            return res
        
        res = change(amount)
    
        return -1 if res >= 1e9 else res