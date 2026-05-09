class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # track the max achivable index
        mai = 0
        i = 0
        n = len(nums)
        while i <= mai and i < n:
            mai = max(mai, i+ nums[i])
            i+=1 
        
        return mai >= n-1
        
            

