class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heap
        h = [] # store top k smallest
        for x in nums:
            heapq.heappush(h,x)
            if len(h) > k:
                heapq.heappop(h)
        res = heapq.heappop(h)
        return res