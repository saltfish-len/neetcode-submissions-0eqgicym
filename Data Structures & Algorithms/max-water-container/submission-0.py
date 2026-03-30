class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # vol = min(h1,h2)*width
        n = len(heights)
        l=0
        r=n-1
        vol = 0
        while l < r:
            vol =max(vol, min(heights[l],heights[r])*(r-l))
            if heights[l]<heights[r]:
                l+=1
                continue
            else:
                r-=1
                continue
        return vol

