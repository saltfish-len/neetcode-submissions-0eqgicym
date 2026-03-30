class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # left half
        n = len(nums)
        left = [1] * n # left[i]: product [0,...,i-1]
        for i in range(1,n):
            left[i] = left[i-1]*nums[i-1]
        
        right = [1] * n
        for i in reversed(range(n-1)):
            right[i] = right[i+1]*nums[i+1]
        
        res = [1] * n
        for i in range(n):
            res[i] = left[i]*right[i]
        
        return res
