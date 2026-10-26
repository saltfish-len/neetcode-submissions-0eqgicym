class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0] * n
        prev = 0
        for i in range(n):
            left[i] = max(height[i], prev)
            prev = left[i]
        prev = 0
        for i in reversed(range(n)):
            right = max(height[i], prev)
            prev = right
            left[i] = min(left[i],right)

        res = 0
        for i in range(n):
            res += left[i] - height[i]
        return res