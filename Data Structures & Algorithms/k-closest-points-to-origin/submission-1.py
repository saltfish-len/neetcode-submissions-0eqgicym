class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = [] # min heap with length k
        dist = lambda p: p[0]**2+p[1]**2
        for p in points:
            heapq.heappush(h,(-dist(p),p))
            if len(h) > k:
                heapq.heappop(h)
        
        return [x[1] for x in h]