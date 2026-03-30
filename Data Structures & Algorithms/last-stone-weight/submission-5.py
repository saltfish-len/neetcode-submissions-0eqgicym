class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # use a heap to speed up
        stones=[-s for s in stones]
        heapq.heapify(stones) # not that it is a min heap
        while len(stones)>1:
            h1 = heapq.heappop(stones)
            h2 = heapq.heappop(stones)
            if h1-h2 < 0:
                heapq.heappush(stones, h1-h2)
            
        stones.append(0)
        return -stones[0]
