class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for x in nums:
            count[x] = count.get(x, 0) + 1

        # sort key by value / use a heap
        heap = []
        for key,val in count.items():
            heapq.heappush(heap,(val,key))
            if len(heap) > k:
                heapq.heappop(heap)

        res = [heapq.heappop(heap)[1] for _ in range(k)]
        return res