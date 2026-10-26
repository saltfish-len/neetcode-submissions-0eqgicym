class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # if k does not used up
        # we can extend the window
        # if k used up
        # move the tail to increase k
        count = defaultdict(int)
        maxf = 1
        res = 0
        l = 0
        for r in range(len(s)):
            # add r
            count[s[r]] += 1
            maxf = max(maxf, count[s[r]])
        

            while (r-l+1) - maxf > k:
                # replacement used up
                # move l
                count[s[l]] -= 1
                l += 1
            res = max(res, (r-l+1))
                
                

        return res
                                                
        