class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # binnary search in [max(weights), sum(weights)]
        r = sum(weights)
        l = max(weights)
        
        def check(cap):
            # greedy
            day = 0
            c = cap
            for w in weights:
                if w > c:
                    # cannot fit
                    day += 1
                    if day >= days:
                        return False
                    c = cap
                c -= w
            return day <= days
        res = r 
        while l <= r:
            mid = (l+r)//2 
            if check(mid):
                # reduce cap
                res = min(mid, res)
                r = mid-1
            else:
                # increase
                l = mid+1

        return res

