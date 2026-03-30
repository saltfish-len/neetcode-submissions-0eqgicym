class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # dp[i]: {sum: number fo ways} for all passible with nums[:i]
        # dp[i][s] = sum(dp[i-1][s+-x])
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1,n+1):
            for k,v in dp[i-1].items():
                dp[i][k+nums[i-1]] += v 
                dp[i][k-nums[i-1]] += v 

        return dp[-1][target]
         
