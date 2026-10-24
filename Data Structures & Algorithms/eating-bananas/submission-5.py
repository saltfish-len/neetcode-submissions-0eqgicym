class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # hour for each pile: ceil(pile/k)
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l+r)//2

            timeused = 0
            for p in piles:
                timeused += math.ceil(p/k)
            if timeused > h:
                # too slow
                l = k+1
            else:
                # can reduce
                r = k-1
                res = k
            


        return res
