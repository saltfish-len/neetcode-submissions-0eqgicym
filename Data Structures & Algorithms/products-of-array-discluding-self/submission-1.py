class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [0] * n
        right = [0] * n
        prev = 1
        for i,x in enumerate(nums):
            left[i] = prev
            prev *= x
        prev = 1
        for i,x in enumerate(reversed(nums)):
            right[n-i-1] = prev*left[n-i-1]
            prev *= x
        
        return right
            