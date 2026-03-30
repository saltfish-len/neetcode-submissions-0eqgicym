class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l=0
        res = 0
        maxf = 0 # number of max fraquence char
        for r in range(len(s)):
            # extend
            count[s[r]] = 1+count.get(s[r],0)
            maxf = max(maxf,count[s[r]])
            # check if valid
            while r-l+1-maxf>k:
                # move l
                count[s[l]] -= 1
                l+=1
            res = max(res,r-l+1)
        return res

             