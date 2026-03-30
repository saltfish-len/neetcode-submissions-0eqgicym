class Solution:
    def trap(self, height: List[int]) -> int:
        # left
        n = len(height)
        left = [0]*n # left bar
        left[0] = height[0]
        for i in range(1,n):
            left[i] = max(height[i],left[i-1])
        right = [0]*n # right bar
        right[-1] = height[-1]
        for i in reversed(range(n-1)):
            right[i] = max(height[i],right[i+1])

        water=[min(l,r) for l,r in zip(left,right)]

        res = 0
        for w,h in zip(water,height):
            res += w-h
        
        return res

