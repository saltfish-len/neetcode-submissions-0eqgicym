class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0] * n
        right = [0] * n

        prev = 0
        for i in range(n):
            left[i] = max(height[i], prev)
            prev = left[i]
        
        prev = 0
        for i in reversed(range(n)):
            right[i] = max(height[i], prev)
            prev = right[i]

        res = 0
        for i in range(n):
            res += min(left[i],right[i]) - height[i]
        return res