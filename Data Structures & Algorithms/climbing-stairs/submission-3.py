class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[i]: climbStairs(n)
        # dp[i+1]: dp[i] + 1 (1) + dp[i-1] + 1 (2)

        dp = [0] * (n+1)
        if n <= 2:
            return n
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]