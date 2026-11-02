class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        # if one subset can sum to target, true
        # each item can in/out that subset

        # dp[i][j]: can we get summation j with nums[:i+1]
        n = len(nums)
        dp = [[False] * (target+1) for _ in range(n+1)]
        # init
        for i in range(n+1):
            dp[i][0] = True 
        
        for i in range(1,n+1):
            for j in range(1, target+1):
                if nums[i-1] <= j:
                    dp[i][j] = (dp[i-1][j-nums[i-1]] or dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[n][target]