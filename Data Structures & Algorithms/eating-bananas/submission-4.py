class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k max = piles.max(), one pile per hour
        # binnary search on [1,piles.max()]

        def check(k:int)-> bool:
            # return True if can eat all piles in h
            time = 0
            for p in piles:
                # round up
                time += math.ceil(p/k)
            return time <= h
        
        l = 1
        r = max(piles)
        k = r
        while l<=r:
            m = int(l+ float(r-l)/2)
            canEat = check(m)
            if canEat:
                # reduce k
                r = m-1
                k = min(m,k)
            else:
                # increase
                l = m+1
        return k

