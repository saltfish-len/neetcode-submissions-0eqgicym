class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i]: rob nums[0:i+1], include i
        # dp[i]: max(dp[i-1], dp[i-2]+nums[i])
        
        n = len(nums)
        if n == 1: return nums[0]
        if n == 2: return max(nums)

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[1],nums[0])

        for i in range(2,n):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        
        return dp[-1]