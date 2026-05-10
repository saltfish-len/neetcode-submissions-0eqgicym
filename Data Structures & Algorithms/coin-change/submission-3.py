class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] min number of coin for amount i
        # dp[i] = min(dp[i-c] + 1 for c in coins)

        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            cand = [dp[i-c] + 1 for c in coins if i>=c]
            if cand:
                dp[i] = min(cand)

        return -1 if dp[amount] == float('inf') else dp[amount]
