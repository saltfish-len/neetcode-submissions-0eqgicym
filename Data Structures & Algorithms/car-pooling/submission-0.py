class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # sort by to
        trips = sorted(trips, key= lambda x : x[1])
        cur = 0
        drop = []
        while trips:
            n,f,t = trips.pop(0)
            while drop and drop[0][0] <= f:
                cur -= heapq.heappop(drop)[1]
            cur += n
            if cur > capacity: return False
            heapq.heappush(drop, (t,n))

        return True

            