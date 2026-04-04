class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp[i]: max subarray end in i
        # dp[i] = max(dp[i-i]+nums[i], nums[i])

        n = len(nums)

        dp = [x for x in nums] # init by copy

        res = nums[0]
        # left to right 
        for i in range(1,n):
            dp[i] = max(dp[i-1]+nums[i],nums[i])
            res = max(dp[i],res)

        return res
        
